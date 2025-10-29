import json
import PyPDF2

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF file"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")
        return ""

def invoke_bedrock_nova(bedrock_client, prompt: str, max_tokens: int = 500) -> str:
    """Invoke Amazon Bedrock Nova Lite model"""
    try:
        body = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ],
            "inferenceConfig": {
                "max_new_tokens": max_tokens,
                "temperature": 0.7,
                "top_p": 0.9
            }
        })
        
        response = bedrock_client.invoke_model(
            modelId='us.amazon.nova-lite-v1:0',
            body=body,
            contentType='application/json',
            accept='application/json'
        )
        
        response_body = json.loads(response['body'].read())
        return response_body['output']['message']['content'][0]['text']
    
    except Exception as e:
        print(f"Error invoking Bedrock: {e}")
        return ""
