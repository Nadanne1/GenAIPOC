"""
Scenario 2: Bedrock Data Automation
Uses Amazon Bedrock's Data Automation for document processing
"""

import boto3
import time
import json
import os
from typing import List, Dict
from detection import PageAnalysis, get_page_as_bytes


class BedrockDataAutomationScenario:
    def __init__(self, bedrock_data_automation_client, s3_client=None):
        self.bedrock_data_automation = bedrock_data_automation_client
        self.s3 = s3_client or boto3.client('s3')
        self.api_calls = 0
        
        # Use existing BDA project ARN from environment or hardcoded
        self.project_arn = os.getenv('BDA_PROJECT_ARN', 'arn:aws:bedrock:us-east-1:036835297034:data-automation-project/de9668a6cff8')
        
        # S3 bucket for temp storage (will be created if needed)
        self.temp_bucket = os.getenv('BDA_TEMP_BUCKET', 'bedrock-data-automation-temp')
        self.temp_prefix = 'bda-comparison/'
        
    def process_pdf(self, pdf_path: str, page_analyses: List[PageAnalysis]) -> Dict:
        """
        Process PDF using Bedrock Data Automation
        
        Args:
            pdf_path: Path to PDF file
            page_analyses: List of page analyses from detection
            
        Returns:
            Dictionary with results and metrics
        """
        print("\n" + "="*60)
        print("SCENARIO 2: BEDROCK DATA AUTOMATION")
        print("="*60)
        
        start_time = time.time()
        results = []
        
        for page_analysis in page_analyses:
            page_num = page_analysis.page_num
            
            # Get page as bytes
            page_bytes = get_page_as_bytes(pdf_path, page_num)
            
            print(f"🤖 Page {page_num}: Using Bedrock Data Automation")
            
            response = self._invoke_data_automation(page_bytes, page_num)
            self.api_calls += 1
            
            # Store result
            results.append({
                'page': page_num,
                'response': response
            })
        
        total_latency = time.time() - start_time
        
        print(f"\n✅ Bedrock Data Automation processing complete")
        print(f"   Total time: {total_latency:.2f}s")
        print(f"   API calls: {self.api_calls}")
        
        return {
            'results': results,
            'latency': total_latency,
            'api_calls': self.api_calls,
            'text_pages': len([p for p in page_analyses if not p.has_tables]),
            'table_pages': len([p for p in page_analyses if p.has_tables])
        }
    
    def _ensure_project(self):
        """Return the existing Data Automation project ARN"""
        return self.project_arn
    
    def _upload_to_s3(self, document_bytes: bytes, page_num: int) -> str:
        """Upload document page to S3 and return URI"""
        try:
            # Try to create bucket if it doesn't exist
            try:
                self.s3.head_bucket(Bucket=self.temp_bucket)
            except:
                print(f"   📦 Creating S3 bucket: {self.temp_bucket}")
                self.s3.create_bucket(Bucket=self.temp_bucket)
            
            key = f"{self.temp_prefix}page_{page_num}_{int(time.time())}.pdf"
            
            self.s3.put_object(
                Bucket=self.temp_bucket,
                Key=key,
                Body=document_bytes
            )
            
            s3_uri = f"s3://{self.temp_bucket}/{key}"
            return s3_uri
            
        except Exception as e:
            print(f"   ⚠️  S3 upload failed: {e}")
            print(f"   💡 Tip: Set BDA_TEMP_BUCKET in .env to an existing S3 bucket you have access to")
            raise
    
    def _invoke_data_automation(self, document_bytes: bytes, page_num: int) -> Dict:
        """
        Invoke Bedrock Data Automation using invoke_data_automation_async
        """
        try:
            # Upload to S3 (BDA requires S3 URIs)
            input_s3_uri = self._upload_to_s3(document_bytes, page_num)
            output_s3_uri = f"s3://{self.temp_bucket}/{self.temp_prefix}output/"
            
            # Get AWS account ID for the profile ARN
            sts = boto3.client('sts')
            aws_account_id = sts.get_caller_identity().get('Account')
            aws_region = os.getenv('AWS_REGION', 'us-east-1')
            
            # Invoke BDA with correct parameter structure
            params = {
                'inputConfiguration': {
                    's3Uri': input_s3_uri
                },
                'outputConfiguration': {
                    's3Uri': output_s3_uri
                },
                'dataAutomationConfiguration': {
                    'dataAutomationProjectArn': self.project_arn
                },
                'dataAutomationProfileArn': f"arn:aws:bedrock:{aws_region}:{aws_account_id}:data-automation-profile/us.data-automation-v1"
            }
            
            response = self.bedrock_data_automation.invoke_data_automation_async(**params)
            
            # Get the invocation ARN
            invocation_arn = response.get('invocationArn')
            
            # Poll for results (synchronous wait)
            result = self._wait_for_completion(invocation_arn)
            
            return result
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return {'error': str(e)}
    
    def _wait_for_completion(self, invocation_arn: str, max_wait: int = 120) -> Dict:
        """
        Wait for async data automation job to complete
        
        Args:
            invocation_arn: ARN of the invocation
            max_wait: Maximum seconds to wait
            
        Returns:
            Result dictionary
        """
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            try:
                response = self.bedrock_data_automation.get_data_automation_status(
                    invocationArn=invocation_arn
                )
                
                status = response.get('status')
                
                if status == 'Success':
                    # Get the output S3 location
                    output_location = response.get('outputConfiguration', {}).get('s3Uri')
                    return {
                        'status': 'success',
                        'output_location': output_location,
                        'response': response
                    }
                elif status in ['ServiceError', 'ClientError']:
                    return {
                        'status': 'failed',
                        'error': response.get('errorMessage', 'Unknown error')
                    }
                elif status == 'InProgress':
                    # Still processing, wait a bit
                    time.sleep(3)
                else:
                    # Unknown status
                    time.sleep(3)
                
            except Exception as e:
                return {'error': str(e)}
        
        return {
            'status': 'timeout',
            'error': f'Processing did not complete within {max_wait} seconds'
        }
    
    def calculate_cost(self, total_pages: int, pricing_config) -> float:
        """
        Calculate cost per 1000 pages
        
        Args:
            total_pages: Total number of pages processed
            pricing_config: PricingConfig object
            
        Returns:
            Cost per 1000 pages
        """
        if total_pages == 0:
            return 0.0
        
        # Bedrock Data Automation charges per page
        cost_per_1000 = pricing_config.bedrock_data_automation
        
        return cost_per_1000
