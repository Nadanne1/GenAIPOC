"""
Scenario 3: Claude Smart Routing
- Text-only pages → Claude Haiku
- Pages with tables → Claude Sonnet 4.0
"""

import boto3
import time
import json
from typing import List, Dict
from detection import PageAnalysis
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock


class ClaudeSmartRoutingScenario:
    def __init__(self, bedrock_runtime_client, max_workers=5):
        self.bedrock_runtime = bedrock_runtime_client
        self.api_calls = 0
        self.haiku_tokens = {'input': 0, 'output': 0}
        self.sonnet_tokens = {'input': 0, 'output': 0}
        self.max_workers = max_workers  # Parallel workers
        self.token_lock = Lock()  # Thread-safe token counting
        
    def process_pdf(self, pdf_path: str, page_analyses: List[PageAnalysis]) -> Dict:
        """
        Process PDF using Claude with smart model routing (parallel processing)
        
        Args:
            pdf_path: Path to PDF file
            page_analyses: List of page analyses from detection
            
        Returns:
            Dictionary with results and metrics
        """
        print("\n" + "="*60)
        print("SCENARIO 3: CLAUDE SMART ROUTING (Parallel)")
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
                    page_analysis.page_num,
                    page_analysis.has_tables,
                    page_analysis.text_content
                )
                future_to_page[future] = page_analysis
            
            # Collect results as they complete
            for future in as_completed(future_to_page):
                page_analysis = future_to_page[future]
                try:
                    result = future.result()
                    results.append(result)
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
        
        print(f"\n✅ Claude processing complete")
        print(f"   Total time: {total_latency:.2f}s")
        print(f"   API calls: {self.api_calls}")
        print(f"   Text pages (Haiku): {text_pages}")
        print(f"   Table pages (Sonnet 4.0): {table_pages}")
        print(f"   Haiku tokens: {self.haiku_tokens['input']:,} in / {self.haiku_tokens['output']:,} out")
        print(f"   Sonnet tokens: {self.sonnet_tokens['input']:,} in / {self.sonnet_tokens['output']:,} out")
        
        return {
            'results': results,
            'latency': total_latency,
            'api_calls': self.api_calls,
            'text_pages': text_pages,
            'table_pages': table_pages,
            'haiku_tokens': self.haiku_tokens,
            'sonnet_tokens': self.sonnet_tokens
        }
    
    def _process_single_page(self, page_num: int, has_tables: bool, text_content: str) -> Dict:
        """Process a single page (called by parallel workers)"""
        if has_tables:
            print(f"📊 Page {page_num}: Using Claude Sonnet 4.0")
            response = self._invoke_claude_sonnet(text_content)
        else:
            print(f"📝 Page {page_num}: Using Claude Haiku")
            response = self._invoke_claude_haiku(text_content)
        
        return {
            'page': page_num,
            'has_tables': has_tables,
            'response': response
        }
    
    def _invoke_claude_haiku(self, text_content: str) -> Dict:
        """Invoke Claude Haiku for text extraction"""
        try:
            prompt = f"""Extract text from this document page. Return ONLY the extracted text content, no formatting or structure needed.

Document text:
{text_content}

Return only the plain text content."""

            response = self.bedrock_runtime.invoke_model(
                modelId='us.anthropic.claude-3-5-haiku-20241022-v1:0',
                body=json.dumps({
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 4096,
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                })
            )
            
            result = json.loads(response['body'].read())
            
            # Track token usage (thread-safe)
            usage = result.get('usage', {})
            with self.token_lock:
                self.haiku_tokens['input'] += usage.get('input_tokens', 0)
                self.haiku_tokens['output'] += usage.get('output_tokens', 0)
            
            return result
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return {'error': str(e)}
    
    def _invoke_claude_sonnet(self, text_content: str) -> Dict:
        """Invoke Claude Sonnet 4.0 for table extraction"""
        try:
            prompt = f"""Extract text and tables from this document page. Return in simple JSON format:
{{"text": "page text", "tables": [{{"rows": [[cell1, cell2]], "headers": []}}]}}

Document text:
{text_content}

Return compact JSON only."""

            response = self.bedrock_runtime.invoke_model(
                modelId='us.anthropic.claude-sonnet-4-20250514-v1:0',
                body=json.dumps({
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 8192,
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                })
            )
            
            result = json.loads(response['body'].read())
            
            # Track token usage (thread-safe)
            usage = result.get('usage', {})
            with self.token_lock:
                self.sonnet_tokens['input'] += usage.get('input_tokens', 0)
                self.sonnet_tokens['output'] += usage.get('output_tokens', 0)
            
            return result
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return {'error': str(e)}
    
    def calculate_cost(self, haiku_tokens: Dict, sonnet_tokens: Dict, 
                      pricing_config) -> float:
        """
        Calculate cost per 1000 pages based on token usage
        
        Args:
            haiku_tokens: Dict with 'input' and 'output' token counts
            sonnet_tokens: Dict with 'input' and 'output' token counts
            pricing_config: PricingConfig object
            
        Returns:
            Cost per 1000 pages
        """
        # Calculate costs (pricing is per 1M tokens)
        haiku_cost = (
            (haiku_tokens['input'] / 1_000_000) * pricing_config.claude_haiku_input +
            (haiku_tokens['output'] / 1_000_000) * pricing_config.claude_haiku_output
        )
        
        sonnet_cost = (
            (sonnet_tokens['input'] / 1_000_000) * pricing_config.claude_sonnet4_input +
            (sonnet_tokens['output'] / 1_000_000) * pricing_config.claude_sonnet4_output
        )
        
        total_cost = haiku_cost + sonnet_cost
        
        # Extrapolate to per 1000 pages
        total_pages = (haiku_tokens['input'] + sonnet_tokens['input']) / pricing_config.avg_tokens_per_page
        
        if total_pages == 0:
            return 0.0
        
        cost_per_1000 = (total_cost / total_pages) * 1000
        
        return cost_per_1000
