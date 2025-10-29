"""
Main comparison orchestrator
Runs all three scenarios and generates comparison report
"""

import json
import time
from typing import Dict, List
from dataclasses import dataclass, asdict
import pandas as pd


@dataclass
class ScenarioResult:
    scenario_name: str
    total_latency: float
    cost_per_1000_pages: float
    pages_processed: int
    text_pages: int
    table_pages: int
    api_calls: int
    details: Dict


class PDFExtractionComparison:
    def __init__(self, textract_scenario, bedrock_scenario, claude_scenario, pricing_config):
        self.textract = textract_scenario
        self.bedrock = bedrock_scenario
        self.claude = claude_scenario
        self.pricing = pricing_config
        
    def run_all_scenarios(self, pdf_path: str, page_analyses: List, skip_bedrock: bool = False) -> List[ScenarioResult]:
        """
        Run all scenarios and collect results
        
        Args:
            pdf_path: Path to PDF file
            page_analyses: List of page analyses from detection
            skip_bedrock: If True, skip Bedrock Data Automation scenario
            
        Returns:
            List of ScenarioResult objects
        """
        results = []
        
        # Scenario 1: Textract
        print("\n" + "🚀 Starting Scenario 1: AWS Textract")
        textract_result = self.textract.process_pdf(pdf_path, page_analyses)
        textract_cost = self.textract.calculate_cost(
            textract_result['text_pages'],
            textract_result['table_pages'],
            self.pricing
        )
        
        results.append(ScenarioResult(
            scenario_name="AWS Textract",
            total_latency=textract_result['latency'],
            cost_per_1000_pages=textract_cost,
            pages_processed=len(page_analyses),
            text_pages=textract_result['text_pages'],
            table_pages=textract_result['table_pages'],
            api_calls=textract_result['api_calls'],
            details=textract_result
        ))
        
        # Scenario 2: Bedrock Data Automation (optional)
        if not skip_bedrock:
            print("\n" + "🚀 Starting Scenario 2: Bedrock Data Automation")
            bedrock_result = self.bedrock.process_pdf(pdf_path, page_analyses)
            bedrock_cost = self.bedrock.calculate_cost(
                len(page_analyses),
                self.pricing
            )
            
            results.append(ScenarioResult(
                scenario_name="Bedrock Data Automation",
                total_latency=bedrock_result['latency'],
                cost_per_1000_pages=bedrock_cost,
                pages_processed=len(page_analyses),
                text_pages=bedrock_result['text_pages'],
                table_pages=bedrock_result['table_pages'],
                api_calls=bedrock_result['api_calls'],
                details=bedrock_result
            ))
        else:
            print("\n" + "⏭️  Skipping Scenario 2: Bedrock Data Automation (static cost)")
        
        # Scenario 3: Claude Smart Routing
        print("\n" + "🚀 Starting Scenario 3: Claude Smart Routing")
        claude_result = self.claude.process_pdf(pdf_path, page_analyses)
        claude_cost = self.claude.calculate_cost(
            claude_result['haiku_tokens'],
            claude_result['sonnet_tokens'],
            self.pricing
        )
        
        results.append(ScenarioResult(
            scenario_name="Claude Smart Routing",
            total_latency=claude_result['latency'],
            cost_per_1000_pages=claude_cost,
            pages_processed=len(page_analyses),
            text_pages=claude_result['text_pages'],
            table_pages=claude_result['table_pages'],
            api_calls=claude_result['api_calls'],
            details=claude_result
        ))
        
        return results
    
    def generate_comparison_report(self, results: List[ScenarioResult]) -> pd.DataFrame:
        """
        Generate comparison report as DataFrame
        
        Args:
            results: List of ScenarioResult objects
            
        Returns:
            Pandas DataFrame with comparison
        """
        data = []
        for result in results:
            data.append({
                'Scenario': result.scenario_name,
                'Total Latency (s)': f"{result.total_latency:.2f}",
                'Cost per 1000 pages ($)': f"{result.cost_per_1000_pages:.2f}",
                'Pages Processed': result.pages_processed,
                'Text Pages': result.text_pages,
                'Table Pages': result.table_pages,
                'API Calls': result.api_calls
            })
        
        df = pd.DataFrame(data)
        return df
    
    def print_detailed_comparison(self, results: List[ScenarioResult]):
        """
        Print detailed comparison with analysis
        
        Args:
            results: List of ScenarioResult objects
        """
        print("\n" + "="*80)
        print("📊 COMPARISON RESULTS")
        print("="*80)
        
        # Create comparison DataFrame
        df = self.generate_comparison_report(results)
        print("\n" + df.to_string(index=False))
        
        # Show comparison summary
        print("\n" + "📊 COMPARISON SUMMARY")
        print("-"*80)
        
        # Lowest cost
        costs = [(r.scenario_name, r.cost_per_1000_pages) for r in results]
        lowest_cost = min(costs, key=lambda x: x[1])
        print(f"💰 Lowest Cost: {lowest_cost[0]} (${lowest_cost[1]:.2f} per 1000 pages)")
        
        # Fastest latency
        latencies = [(r.scenario_name, r.total_latency) for r in results]
        fastest = min(latencies, key=lambda x: x[1])
        print(f"⚡ Fastest: {fastest[0]} ({fastest[1]:.2f}s)")
        
        # Cost comparison
        print("\n" + "💵 COST ANALYSIS")
        print("-"*80)
        baseline = costs[0][1]  # Textract as baseline
        for name, cost in costs:
            diff = cost - baseline
            pct = ((cost - baseline) / baseline * 100) if baseline > 0 else 0
            symbol = "+" if diff > 0 else ""
            print(f"{name:30s}: ${cost:8.2f}  ({symbol}{pct:+6.1f}% vs Textract)")
        
        # Latency comparison
        print("\n" + "⏱️  LATENCY ANALYSIS")
        print("-"*80)
        baseline_latency = latencies[0][1]  # Textract as baseline
        for name, latency in latencies:
            diff = latency - baseline_latency
            pct = ((latency - baseline_latency) / baseline_latency * 100) if baseline_latency > 0 else 0
            symbol = "+" if diff > 0 else ""
            print(f"{name:30s}: {latency:8.2f}s  ({symbol}{pct:+6.1f}% vs Textract)")
        
        print("\n" + "="*80)
    
    def save_results(self, results: List[ScenarioResult], output_path: str = "comparison_results.json"):
        """
        Save detailed results to JSON file
        
        Args:
            results: List of ScenarioResult objects
            output_path: Path to save JSON file
        """
        output_data = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'scenarios': [asdict(r) for r in results]
        }
        
        with open(output_path, 'w') as f:
            json.dump(output_data, f, indent=2)
        
        print(f"\n💾 Results saved to: {output_path}")
