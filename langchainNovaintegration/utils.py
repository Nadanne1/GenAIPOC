import json
import PyPDF2
import os
from IPython.display import Image, display
from langchain_core.runnables.graph import MermaidDrawMethod
import nest_asyncio


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

# def invoke_bedrock_nova(bedrock_client, prompt: str, max_tokens: int = 500) -> str:
#     """Invoke Amazon Bedrock Nova Lite model"""
#     try:
#         body = json.dumps({
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": [{"text": prompt}]
#                 }
#             ],
#             "inferenceConfig": {
#                 "max_new_tokens": max_tokens,
#                 "temperature": 0.7,
#                 "top_p": 0.9
#             }
#         })
        
#         response = bedrock_client.invoke_model(
#             modelId='us.amazon.nova-lite-v1:0',
#             body=body,
#             contentType='application/json',
#             accept='application/json'
#         )
        
#         response_body = json.loads(response['body'].read())
#         return response_body['output']['message']['content'][0]['text']
    
#     except Exception as e:
#         print(f"Error invoking Bedrock: {e}")
#         return ""


def show_graph(graph, xray=False):
    """Display a LangGraph mermaid diagram with fallback rendering.
    
    Handles timeout errors from mermaid.ink by falling back to pyppeteer.
    
    Args:
        graph: The LangGraph object that has a get_graph() method
    """
    from IPython.display import Image
    try:
        # Try the default renderer first
        return Image(graph.get_graph(xray=xray).draw_mermaid_png())
    except Exception as e:
        # Fall back to pyppeteer if the default renderer fails
        nest_asyncio.apply()
        return Image(graph.get_graph().draw_mermaid_png(draw_method=MermaidDrawMethod.PYPPETEER))