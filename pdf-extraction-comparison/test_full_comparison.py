"""
Full comparison test - Textract vs Claude Smart Routing
Both with parallel processing for fair comparison
"""

import sys
sys.path.insert(0, 'pdf-extraction-comparison')

from detection import detect_tables_in_pdf
from scenario_textract import TextractScenario
from scenario_claude import ClaudeSmartRoutingScenario
import boto3
import os
import time
import json
from dotenv import load_dotenv

# Load environment
load_dotenv('pdf-extraction-comparison/.env')

pdf_path = 'pdf-extraction-comparison/amzn-20241231.pdf'

print("="*80)
print("FULL COMPARISON: TEXTRACT vs CLAUDE SMART ROUTING")
print("Both with parallel processing")
print("="*80)
print(f"\n📄 PDF: {pdf_path}\n")

# Initialize AWS clients
session = boto3.Session(region_name=os.getenv('AWS_REGION', 'us-east-1'))
textract = session.client('textract')
bedrock_runtime = session.client('bedrock-runtime', region_name='us-east-1')

print("✅ AWS clients initialized\n")

# Step 1: Detect tables
print("STEP 1: TABLE DETECTION")
print("-"*80)
page_analyses = detect_tables_in_pdf(pdf_path)

text_pages = len([p for p in page_analyses if not p.has_tables])
table_pages = len([p for p in page_analyses if p.has_tables])

# Step 2: Run Textract (parallel)
print("\nSTEP 2: AWS TEXTRACT (PARALLEL)")
print("-"*80)

textract_scenario = TextractScenario(textract, max_workers=10)
textract_start = time.time()
textract_result = textract_scenario.process_pdf(pdf_path, page_analyses)
textract_time = time.time() - textract_start

# Calculate Textract costs
textract_text_cost = (text_pages / 1000) * 1.50
textract_table_cost = (table_pages / 1000) * 15.00
textract_total_cost = textract_text_cost + textract_table_cost
textract_per_1000 = (textract_total_cost / 117) * 1000

# Step 3: Run Claude Smart Routing (parallel)
print("\nSTEP 3: CLAUDE SMART ROUTING (PARALLEL)")
print("-"*80)

claude_scenario = ClaudeSmartRoutingScenario(bedrock_runtime, max_workers=5)
claude_start = time.time()
claude_result = claude_scenario.process_pdf(pdf_path, page_analyses)
claude_time = time.time() - claude_start

# Calculate Claude costs
haiku_tokens = claude_result['haiku_tokens']
sonnet_tokens = claude_result['sonnet_tokens']

haiku_cost = (
    (haiku_tokens['input'] / 1_000_000) * 0.80 +
    (haiku_tokens['output'] / 1_000_000) * 4.00
)

sonnet_cost = (
    (sonnet_tokens['input'] / 1_000_000) * 3.00 +
    (sonnet_tokens['output'] / 1_000_000) * 15.00
)

claude_total_cost = haiku_cost + sonnet_cost
claude_per_1000 = (claude_total_cost / 117) * 1000

# Step 4: Comparison
print("\n" + "="*80)
print("📊 FINAL COMPARISON")
print("="*80)

print(f"\n💰 COST COMPARISON:")
print(f"   Textract:")
print(f"     - Text pages: {text_pages} × $1.50/1000 = ${textract_text_cost:.4f}")
print(f"     - Table pages: {table_pages} × $15.00/1000 = ${textract_table_cost:.4f}")
print(f"     - Total: ${textract_total_cost:.4f}")
print(f"     - Per 1000 pages: ${textract_per_1000:.2f}")

print(f"\n   Claude Smart Routing:")
print(f"     - Haiku cost: ${haiku_cost:.4f}")
print(f"     - Sonnet cost: ${sonnet_cost:.4f}")
print(f"     - Total: ${claude_total_cost:.4f}")
print(f"     - Per 1000 pages: ${claude_per_1000:.2f}")

cost_savings = textract_total_cost - claude_total_cost
cost_savings_pct = (cost_savings / textract_total_cost * 100) if textract_total_cost > 0 else 0

print(f"\n   💵 Cost Difference: ", end="")
if cost_savings > 0:
    print(f"Claude costs ${cost_savings:.4f} less ({cost_savings_pct:.1f}% savings)")
else:
    print(f"Textract costs ${-cost_savings:.4f} less ({-cost_savings_pct:.1f}% savings)")

print(f"\n⏱️  LATENCY COMPARISON:")
print(f"   Textract: {textract_time:.2f}s ({textract_time/60:.1f} min)")
print(f"   Claude: {claude_time:.2f}s ({claude_time/60:.1f} min)")

latency_diff = textract_time - claude_time
latency_diff_pct = (latency_diff / textract_time * 100) if textract_time > 0 else 0

print(f"\n   ⚡ Latency Difference: ", end="")
if latency_diff > 0:
    print(f"Claude is {latency_diff:.2f}s faster ({latency_diff_pct:.1f}%)")
else:
    print(f"Textract is {-latency_diff:.2f}s faster ({-latency_diff_pct:.1f}%)")

# Step 5: Save extraction results to S3
print("\n" + "="*80)
print("SAVING EXTRACTION RESULTS TO S3")
print("="*80)

s3 = session.client('s3')
output_bucket = os.getenv('OUTPUT_BUCKET', 'bedrock-data-automation-temp-suralink')
document_id = 'amzn-20241231'

# Save Textract results to S3
textract_output_key = f'textract-output/{document_id}.json'
s3.put_object(
    Bucket=output_bucket,
    Key=textract_output_key,
    Body=json.dumps(textract_result, indent=2),
    ContentType='application/json'
)
print(f"✅ Textract results saved to: s3://{output_bucket}/{textract_output_key}")

# Save Claude results to S3
claude_output_key = f'claude-output/{document_id}.json'
s3.put_object(
    Bucket=output_bucket,
    Key=claude_output_key,
    Body=json.dumps(claude_result, indent=2),
    ContentType='application/json'
)
print(f"✅ Claude results saved to: s3://{output_bucket}/{claude_output_key}")

# Step 6: Save comparison summary
print("\n" + "="*80)
print("SAVING COMPARISON SUMMARY")
print("="*80)

output_data = {
    "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
    "document": {
        "path": pdf_path,
        "total_pages": 117,
        "text_pages": text_pages,
        "table_pages": table_pages
    },
    "textract": {
        "latency_seconds": textract_time,
        "latency_minutes": textract_time / 60,
        "costs": {
            "text_pages_cost": textract_text_cost,
            "table_pages_cost": textract_table_cost,
            "total_cost": textract_total_cost,
            "cost_per_1000_pages": textract_per_1000
        },
        "api_calls": textract_result['api_calls'],
        "parallel_workers": 10
    },
    "claude_smart_routing": {
        "latency_seconds": claude_time,
        "latency_minutes": claude_time / 60,
        "tokens": {
            "haiku": haiku_tokens,
            "sonnet": sonnet_tokens
        },
        "costs": {
            "haiku_cost": haiku_cost,
            "sonnet_cost": sonnet_cost,
            "total_cost": claude_total_cost,
            "cost_per_1000_pages": claude_per_1000
        },
        "api_calls": claude_result['api_calls'],
        "parallel_workers": 5
    },
    "comparison": {
        "cost": {
            "savings_amount": cost_savings,
            "savings_percentage": cost_savings_pct,
            "lower_cost": "Claude" if cost_savings > 0 else "Textract"
        },
        "latency": {
            "difference_seconds": latency_diff,
            "difference_percentage": latency_diff_pct,
            "faster": "Claude" if latency_diff > 0 else "Textract"
        },
        "trade_off": "Cost vs Speed - each approach has advantages"
    }
}

# Save comparison summary locally
output_file = 'pdf-extraction-comparison/full_comparison_results.json'
with open(output_file, 'w') as f:
    json.dump(output_data, f, indent=2)
print(f"✅ Comparison summary saved locally: {output_file}")

# Save comparison summary to S3
comparison_key = f'comparison/{document_id}_summary.json'
s3.put_object(
    Bucket=output_bucket,
    Key=comparison_key,
    Body=json.dumps(output_data, indent=2),
    ContentType='application/json'
)
print(f"✅ Comparison summary saved to S3: s3://{output_bucket}/{comparison_key}")
print("\n✅ Comparison complete!")
print("="*80)
