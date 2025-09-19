# GenAI Proof of Concepts (POCs)

A collection of Generative AI proof-of-concept projects demonstrating various AI capabilities and use cases using AWS services and other AI platforms.

## 📁 Available POCs

### 1. [PDF to Markdown Converter](./pdf-to-markdown-poc/)
**Status**: ✅ Complete  
**Technologies**: AWS Bedrock (Claude Sonnet 4.0), S3, PyMuPDF, Python  
**Description**: Converts PDF documents to clean Markdown format with intelligent text extraction and image handling.

**Key Features**:
- Extracts text and images from PDFs
- AI-powered conversion using Claude
- S3 integration for storage
- Batch processing capabilities
- Handles large documents with chunking

---

## 🚀 Getting Started

Each POC is contained in its own directory with:
- Complete documentation
- Installation instructions
- Usage examples
- Configuration guides
- Troubleshooting tips

Navigate to any POC folder to get started with that specific project.

## 🛠️ Common Prerequisites

Most POCs in this repository require:
- Python 3.8+
- AWS Account with appropriate permissions
- Access to AWS Bedrock (varies by POC)
- Jupyter Notebook environment

## 📋 POC Template Structure

Each POC follows this structure:
```
poc-name/
├── README.md           # Detailed documentation
├── notebook.ipynb      # Main implementation
├── requirements.txt    # Dependencies (if applicable)
├── .env.example       # Environment variables template
├── LICENSE            # MIT License
└── assets/            # Supporting files, images, etc.
```

## 🔒 License & Liability

Each POC includes an MIT License that:
- Provides the software "as-is" without warranty
- Protects contributors from liability
- Allows free use, modification, and distribution
- Requires attribution to original authors

## 🤝 Contributing

When adding new POCs:

1. Create a new folder with a descriptive name
2. Follow the template structure above
3. Include comprehensive documentation
4. Add your POC to the list in this README
5. Test thoroughly before committing
6. Include proper error handling and logging

## 📞 Support

For questions or issues:
- Check the individual POC documentation
- Review troubleshooting sections
- Open an issue in this repository

## 🗺️ Roadmap

Future POCs may include:
- Document summarization with different AI models
- Image analysis and description generation
- Code generation and review tools
- Natural language to SQL conversion
- Multi-modal AI applications
- RAG (Retrieval Augmented Generation) implementations

---

**Note**: This repository is for educational and proof-of-concept purposes. Each POC demonstrates specific AI capabilities and should be adapted for production use with appropriate security, monitoring, and error handling considerations.