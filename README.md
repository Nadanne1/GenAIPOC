# PDF to Markdown Converter

A Python-based tool that converts PDF documents to Markdown format using AWS services. The tool extracts text and images from PDFs stored in S3, processes them with Claude AI via AWS Bedrock, and outputs clean Markdown files with embedded image references.

## Features

- **PDF Processing**: Extracts text and images from PDF documents using PyMuPDF
- **AI-Powered Conversion**: Uses Claude Sonnet 4.0 via AWS Bedrock for intelligent Markdown conversion
- **S3 Integration**: Reads PDFs from S3 and stores outputs (Markdown + images) back to S3
- **Image Handling**: Automatically extracts and uploads images with proper Markdown references
- **Batch Processing**: Support for processing multiple PDFs in one operation
- **Chunked Processing**: Handles large documents by processing them in chunks
- **Fallback Conversion**: Basic conversion method if AI processing fails

## Prerequisites

- Python 3.8+
- AWS Account with appropriate permissions
- Access to AWS Bedrock (Claude Sonnet 4.0)
- S3 buckets for input and output

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd genai-poc
   ```

2. **Install required packages**:
   ```bash
   # Using conda (recommended)
   conda install -c conda-forge python-dotenv pymupdf pandas boto3 ipython

   # Or using pip
   pip install python-dotenv pymupdf pandas boto3 ipython
   ```

3. **Set up AWS credentials**:
   - Configure AWS CLI: `aws configure`
   - Or set environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`
   - Ensure your AWS account has access to Bedrock and the Claude Sonnet 4.0 model

## Configuration

Create a `.env` file in the project root with your settings:

```env
# AWS Configuration
AWS_REGION=us-east-1
BEDROCK_REGION=us-east-1

# S3 Bucket Configuration
INPUT_BUCKET=your-input-bucket-name
OUTPUT_BUCKET=your-output-bucket-name
IMAGES_FOLDER=extracted_images
```

## Usage

### Using Jupyter Notebook

1. **Start Jupyter**:
   ```bash
   jupyter notebook
   ```

2. **Open the notebook**: `pdftomarkdown.ipynb`

3. **Run the setup cells** (Cells 1-3) to initialize the environment

4. **Process a single PDF**:
   ```python
   # Example: Process a PDF from your input bucket
   summary, markdown_content = process_pdf(
       input_bucket="your-input-bucket",
       pdf_key="path/to/your/document.pdf"
   )
   ```

5. **List available PDFs**:
   ```python
   # List all PDFs in your input bucket
   pdf_files = list_pdfs_in_bucket("your-input-bucket")
   ```

6. **Batch process multiple PDFs**:
   ```python
   # Process multiple PDFs at once
   results = batch_process_pdfs("your-input-bucket", pdf_files, max_files=5)
   ```

7. **Preview generated Markdown**:
   ```python
   # Preview the converted Markdown
   preview_markdown(markdown_content, max_lines=50)
   ```

### Key Functions

- `process_pdf(bucket, pdf_key)` - Process a single PDF file
- `list_pdfs_in_bucket(bucket)` - List all PDF files in a bucket
- `batch_process_pdfs(bucket, pdf_list)` - Process multiple PDFs
- `preview_markdown(content)` - Preview generated Markdown

## AWS Permissions Required

Your AWS user/role needs the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::your-input-bucket/*",
                "arn:aws:s3:::your-output-bucket/*",
                "arn:aws:s3:::your-input-bucket",
                "arn:aws:s3:::your-output-bucket"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": "arn:aws:bedrock:us-east-1::foundation-model/us.anthropic.claude-sonnet-4-20250514-v1:0"
        }
    ]
}
```

## Output Structure

The tool creates the following output structure in your S3 bucket:

```
output-bucket/
├── document.md                    # Converted Markdown file
└── extracted_images/              # Extracted images folder
    ├── document_page_1_img_1.png
    ├── document_page_1_img_2.png
    └── ...
```

## Configuration Options

You can customize the processing behavior by modifying the `Config` class:

- `MAX_PAGES_PER_CHUNK`: Number of pages to process in each chunk (default: 5)
- `MAX_INPUT_TOKENS`: Maximum input tokens for Claude (default: 150,000)

## Troubleshooting

### Common Issues

1. **AWS Credentials Error**:
   - Ensure AWS credentials are properly configured
   - Check that your region settings match your resources

2. **Bedrock Access Denied**:
   - Verify you have access to AWS Bedrock in your region
   - Ensure the Claude Sonnet 4.0 model is available in your account

3. **S3 Permission Errors**:
   - Check bucket permissions and policies
   - Verify bucket names in your configuration

4. **Large Document Processing**:
   - The tool automatically chunks large documents
   - Adjust `MAX_PAGES_PER_CHUNK` if needed

### Debug Mode

Enable detailed logging by checking the notebook output cells for processing status and error messages.

## Example Workflow

1. Upload your PDF files to the input S3 bucket
2. Run the Jupyter notebook
3. Execute the processing cells
4. Check the output bucket for:
   - Converted Markdown files
   - Extracted images in the `extracted_images/` folder
5. Download and review the generated Markdown

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Check the troubleshooting section above
- Review AWS Bedrock and S3 documentation
- Open an issue in the repository