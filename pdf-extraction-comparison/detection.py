"""
PDF Table Detection Module
Uses PyMuPDF to detect if pages contain tables
"""

import fitz  # PyMuPDF
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PageAnalysis:
    page_num: int
    has_tables: bool
    text_length: int
    table_count: int
    text_content: str = ""


def detect_tables_in_pdf(pdf_path: str) -> List[PageAnalysis]:
    """
    Analyze PDF and detect which pages contain tables
    
    Args:
        pdf_path: Path to PDF file
        
    Returns:
        List of PageAnalysis objects for each page
    """
    doc = fitz.open(pdf_path)
    page_analyses = []
    
    print(f"📄 Analyzing {len(doc)} pages for table detection...")
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        
        # Extract text
        text = page.get_text()
        
        # Detect tables using PyMuPDF
        tables = page.find_tables()
        table_list = list(tables) if tables else []
        has_tables = len(table_list) > 0
        
        analysis = PageAnalysis(
            page_num=page_num + 1,
            has_tables=has_tables,
            text_length=len(text),
            table_count=len(table_list),
            text_content=text
        )
        
        page_analyses.append(analysis)
        
        status = "📊 Tables" if has_tables else "📝 Text only"
        print(f"  Page {page_num + 1}: {status} ({len(table_list)} tables, {len(text)} chars)")
    
    doc.close()
    
    # Summary
    total_pages = len(page_analyses)
    table_pages = sum(1 for p in page_analyses if p.has_tables)
    text_pages = total_pages - table_pages
    
    print(f"\n✅ Detection complete:")
    print(f"   Total pages: {total_pages}")
    print(f"   Text-only pages: {text_pages}")
    print(f"   Pages with tables: {table_pages}")
    
    return page_analyses


def get_page_as_bytes(pdf_path: str, page_num: int) -> bytes:
    """
    Extract a single page as bytes for API calls
    
    Args:
        pdf_path: Path to PDF file
        page_num: Page number (1-indexed)
        
    Returns:
        Page as bytes
    """
    doc = fitz.open(pdf_path)
    
    # Create a new PDF with just this page
    new_doc = fitz.open()
    new_doc.insert_pdf(doc, from_page=page_num - 1, to_page=page_num - 1)
    
    # Get as bytes
    page_bytes = new_doc.tobytes()
    
    new_doc.close()
    doc.close()
    
    return page_bytes
