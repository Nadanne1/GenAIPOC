"""
Scenario 1: AWS Textract
- Text-only pages → DetectDocumentText API
- Pages with tables → AnalyzeDocument API (TABLES)
"""

import boto3
import time
from typing import List, Dict
from detection import PageAnalysis, get_page_as_bytes
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock


class TextractScenario:
    def __init__(self, textract_client, max_workers=10):
        self.textract = textract_client
        self.api_calls = 0
        self.max_workers = max_workers  # Textract can handle more parallel requests
        self.api_lock = Lock()  # Thread-safe API call counting
        
    def process_pdf(self, pdf_path: str, page_analyses: List[PageAnalysis]) -> Dict:
        """
        Process PDF using Textract with smart routing (parallel processing)
        
        Args:
            pdf_path: Path to PDF file
            page_analyses: List of page analyses from detection
            
        Returns:
            Dictionary with results and metrics
        """
        print("\n" + "="*60)
        print("SCENARIO 1: AWS TEXTRACT (Parallel)")
        print(f"Processing {len(page_analyses)} pages with {self.max_workers} workers")
        print("="*60)
        
        start_time = time.time()
        results = []
        
        # Process pages in parallel
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            future_to_page = {}
            for page_analysis in page_analyses:
                future = executor.submit(
                    self._process_single_page,
                    pdf_path,
                    page_analysis.page_num,
                    page_analysis.has_tables
                )
                future_to_page[future] = page_analysis
            
            # Collect results as they complete
            for future in as_completed(future_to_page):
                page_analysis = future_to_page[future]
                try:
                    result = future.result()
                    results.append(result)
                    with self.api_lock:
                        self.api_calls += 1
                except Exception as e:
                    print(f"   ❌ Page {page_analysis.page_num} failed: {e}")
                    results.append({
                        'page': page_analysis.page_num,
                        'has_tables': page_analysis.has_tables,
                        'response': {'error': str(e)}
                    })
        
        # Sort results by page number
        results.sort(key=lambda x: x['page'])
        
        # Count page types
        text_pages = sum(1 for r in results if not r['has_tables'])
        table_pages = sum(1 for r in results if r['has_tables'])
        
        total_latency = time.time() - start_time
        
        print(f"\n✅ Textract processing complete")
        print(f"   Total time: {total_latency:.2f}s")
        print(f"   API calls: {self.api_calls}")
        print(f"   Text pages: {text_pages}")
        print(f"   Table pages: {table_pages}")
        
        return {
            'results': results,
            'latency': total_latency,
            'api_calls': self.api_calls,
            'text_pages': text_pages,
            'table_pages': table_pages
        }
    
    def _process_single_page(self, pdf_path: str, page_num: int, has_tables: bool) -> Dict:
        """Process a single page (called by parallel workers)"""
        # Get page as bytes
        page_bytes = get_page_as_bytes(pdf_path, page_num)
        
        if has_tables:
            print(f"📊 Page {page_num}: Using AnalyzeDocument (TABLES)")
            response = self._analyze_document_tables(page_bytes)
        else:
            print(f"📝 Page {page_num}: Using DetectDocumentText")
            response = self._detect_document_text(page_bytes)
        
        return {
            'page': page_num,
            'has_tables': has_tables,
            'response': response
        }
    
    def _detect_document_text(self, document_bytes: bytes) -> Dict:
        """Call Textract DetectDocumentText API"""
        try:
            response = self.textract.detect_document_text(
                Document={'Bytes': document_bytes}
            )
            return response
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return {'error': str(e)}
    
    def _analyze_document_tables(self, document_bytes: bytes) -> Dict:
        """Call Textract AnalyzeDocument API with TABLES feature"""
        try:
            response = self.textract.analyze_document(
                Document={'Bytes': document_bytes},
                FeatureTypes=['TABLES']
            )
            return response
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return {'error': str(e)}
    
    def calculate_cost(self, text_pages: int, table_pages: int, 
                      pricing_config) -> float:
        """
        Calculate cost per 1000 pages
        
        Args:
            text_pages: Number of text-only pages
            table_pages: Number of pages with tables
            pricing_config: PricingConfig object
            
        Returns:
            Cost per 1000 pages
        """
        total_pages = text_pages + table_pages
        
        if total_pages == 0:
            return 0.0
        
        # Calculate actual cost for processed pages
        text_cost = (text_pages / 1000) * pricing_config.textract_detect_text
        table_cost = (table_pages / 1000) * pricing_config.textract_analyze_tables
        total_cost = text_cost + table_cost
        
        # Extrapolate to 1000 pages
        cost_per_1000 = (total_cost / total_pages) * 1000
        
        return cost_per_1000
