"""
Main script to run PDF extraction comparison
"""

import boto3
import os
from dotenv import load_dotenv

from detection import detect_tables_in_pdf
from scenario_textract import TextractScenario
from scenario_bedrock_data_automation import BedrockDataAutomationScenario
from scenario_claude import ClaudeSmartRoutingScenario
from comparison import PDFExtractionComparison
from dataclasses import dataclass


@dataclass
class PricingConfig:
    """Pricing per 1000 pages/units"""
    # Textract pricing (per 1000 pages)
    textract_detect_text: float = 1.50
    textract_analyze_tables: float = 15.00
    
    # Bedrock Data Automation (per 1000 pages)
    bedrock_data_automation: float = 10.00  # Approximate
    
    # Claude pricing (per 1M tokens)
    # Claude 3.5 Haiku pricing
    claude_haiku_input: float = 0.80
    claude_haiku_output: float = 4.00
    # Claude Sonnet 4.0 pricing
    claude_sonnet4_input: float = 3.00
    claude_sonnet4_output: float = 15.00
    
    # Average tokens per page (estimate)
    avg_tokens_per_page: int = 500


def main(pdf_path: str):
    """
    Run complete PDF extraction comparison
    
    Args:
        pdf_path: Path to PDF file to analyze
    """
    print("="*80)
    print("PDF EXTRACTION COMPARISON DEMO")
    print("="*80)
    print(f"\n📄 PDF: {pdf_path}\n")
    
    # Load environment variables from the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(script_dir, '.env')
    load_dotenv(env_path)
    
    # Initialize AWS clients
    session = boto3.Session(region_name=os.getenv('AWS_REGION', 'us-east-1'))
    s3 = session.client('s3')
    textract = session.client('textract')
    bedrock_runtime = session.client('bedrock-runtime', region_name='us-east-1')
    bedrock_data_automation = session.client('bedrock-data-automation-runtime', region_name='us-east-1')
    
    print("✅ AWS clients initialized\n")
    
    # Step 1: Detect tables in PDF
    print("STEP 1: TABLE DETECTION")
    print("-"*80)
    page_analyses = detect_tables_in_pdf(pdf_path)
    
    # Step 2: Initialize scenarios
    print("\n" + "STEP 2: INITIALIZING SCENARIOS")
    print("-"*80)
    
    pricing = PricingConfig()
    
    textract_scenario = TextractScenario(textract)
    bedrock_scenario = BedrockDataAutomationScenario(bedrock_data_automation, s3)
    claude_scenario = ClaudeSmartRoutingScenario(bedrock_runtime)
    
    print("✅ All scenarios initialized")
    
    # Step 3: Run comparison
    print("\n" + "STEP 3: RUNNING SCENARIOS")
    print("-"*80)
    
    comparison = PDFExtractionComparison(
        textract_scenario,
        bedrock_scenario,
        claude_scenario,
        pricing
    )
    
    results = comparison.run_all_scenarios(pdf_path, page_analyses, skip_bedrock=True)
    
    # Step 4: Generate and display report
    print("\n" + "STEP 4: GENERATING REPORT")
    print("-"*80)
    
    comparison.print_detailed_comparison(results)
    
    # Step 5: Save results
    comparison.save_results(results)
    
    print("\n✅ Comparison complete!")
    
    return results


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_pdf>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)
    
    main(pdf_path)
