# PDF Extraction Cost & Latency Comparison

A comprehensive comparison framework for evaluating different AWS-based PDF extraction approaches, focusing on **cost per 1000 pages** and **processing latency**.

## 🎯 Purpose

Compare three approaches for extracting text and tables from PDF documents:
1. **AWS Textract** - Smart routing between text and table APIs
2. **Amazon Bedrock Data Automation** - Managed document processing service
3. **Claude Smart Routing** - Intelligent model selection (Haiku for text, Sonnet 4.0 for tables)

## 🏗️ Architecture

```
PDF Document
    ↓
[PyMuPDF Detection] → Identifies text-only vs table pages
    ↓
┌─────────────────┬──────────────────────┬────────────────────────┐
│   Textract      │  Bedrock Data Auto   │  Claude Smart Routing  │
│  (Parallel)     │                      │     (Parallel)         │
├─────────────────┼──────────────────────┼────────────────────────┤
│ Text → $1.50/1K │  All → $10.00/1K    │ Text → Haiku (cheap)   │
│ Table → $15/1K  │                      │ Table → Sonnet (accurate)│
└─────────────────┴──────────────────────┴────────────────────────┘
    ↓
Cost & Latency Comparison → S3 Output
```

## ✨ Features

- **Intelligent Detection**: PyMuPDF automatically detects tables in each page
- **Parallel Processing**: Both Textract (10 workers) and Claude (5 workers) process pages concurrently
- **Smart Routing**: Uses the most cost-effective API/model for each page type
- **Real Cost Tracking**: Calculates actual costs based on API usage and token consumption
- **S3 Integration**: Saves extraction results and comparison summary to S3
- **Thread-Safe**: Proper locking for concurrent token counting

## 📋 Prerequisites

- Python 3.9+
- AWS Account with:
  - Amazon Textract access
  - Amazon Bedrock access (Claude models)
  - Amazon Bedrock Data Automation (optional)
  - S3 bucket for outputs
- AWS credentials configured

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd pdf-extraction-comparison

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your AWS credentials
nano .env
```

Required environment variables:
```bash
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
BDA_TEMP_BUCKET=your-s3-bucket
OUTPUT_BUCKET=your-output-bucket
```

### 3. Run Comparison

```bash
# Full comparison (Textract + Claude)
python3 test_full_comparison.py

# Or use main.py for all three scenarios
python3 main.py path/to/your/document.pdf
```

## 📊 Output

### Console Output
```
📊 FINAL COMPARISON
================================================================================
💰 COST COMPARISON:
   Textract: $0.69 (79 text pages + 38 table pages)
   Claude Smart Routing: $0.45
   💵 Difference: Claude costs $0.24 less (34.8% savings)

⏱️  LATENCY COMPARISON:
   Textract: 4.2 minutes
   Claude: 12.5 minutes
   ⚡ Difference: Textract is 8.3 minutes faster
```

### S3 Output Structure
```
s3://your-bucket/
├── textract-output/
│   └── document_id.json          # Full Textract results
├── claude-output/
│   └── document_id.json          # Full Claude results
└── comparison/
    └── document_id_summary.json  # Cost/latency comparison
```

## 💰 Pricing (as of 2025)

| Service | Text Pages | Table Pages |
|---------|-----------|-------------|
| **Textract** | $1.50/1000 | $15.00/1000 |
| **Bedrock DA** | $10.00/1000 | $10.00/1000 |
| **Claude Haiku 3.5** | $0.80/1M input tokens | - |
| **Claude Sonnet 4.0** | $3.00/1M input tokens | $15.00/1M output tokens |

## 🔧 Key Components

### Detection (`detection.py`)
- Uses PyMuPDF to analyze each page
- Detects tables using `find_tables()`
- Returns page metadata for routing decisions

### Textract Scenario (`scenario_textract.py`)
- Parallel processing with 10 workers
- Smart API routing based on content type
- Thread-safe API call counting

### Claude Scenario (`scenario_claude.py`)
- Parallel processing with 5 workers
- Model selection: Haiku (text) vs Sonnet 4.0 (tables)
- Thread-safe token tracking

### Comparison (`test_full_comparison.py`)
- Runs both scenarios
- Calculates costs and latency
- Saves results to S3

## 🎓 Use Cases

- **Cost Optimization**: Determine the most cost-effective extraction method for your document mix
- **Performance Benchmarking**: Compare latency across different services
- **Smart Routing**: Implement intelligent routing based on content type
- **Proof of Concept**: Demonstrate cost savings with AI-powered extraction

## 📝 Example Results

For a 117-page financial document (79 text, 38 tables):

| Metric | Textract | Claude Smart |
|--------|----------|--------------|
| **Cost** | $0.69 | $0.45 |
| **Latency** | 4.2 min | 12.5 min |
| **Trade-off** | Faster | Lower cost (35% savings) |

## 🔒 Security Notes

- Never commit `.env` files with real credentials
- Use IAM roles in production instead of access keys
- Rotate credentials regularly
- Use S3 bucket policies to restrict access

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🙋 Support

For issues or questions:
- Open a GitHub issue
- Check existing documentation
- Review AWS service documentation

## 🔗 Related Resources

- [AWS Textract Documentation](https://docs.aws.amazon.com/textract/)
- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)
- [Anthropic Claude Pricing](https://www.anthropic.com/pricing)

---

**Built with ❤️ for cost-conscious document processing**
