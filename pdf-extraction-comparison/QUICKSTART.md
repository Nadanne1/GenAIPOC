# Quick Start Guide

## 5-Minute Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure AWS
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your AWS credentials
# Required: AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, OUTPUT_BUCKET
```

### 3. Run the Comparison
```bash
# Full comparison (Textract + Claude)
python3 test_full_comparison.py

# Or specify your own PDF
python3 main.py path/to/your/document.pdf
```

That's it! 🎉

---

## What You'll Get

### Console Output
- Real-time processing progress
- Cost breakdown by service
- Latency comparison
- Trade-off analysis

### S3 Output
```
s3://your-bucket/
├── textract-output/document.json
├── claude-output/document.json
└── comparison/document_summary.json
```

---

## Example Results

For a 117-page document (79 text, 38 tables):

```
💰 COST COMPARISON:
   Textract: $0.69
   Claude Smart Routing: $0.45
   Difference: Claude costs 35% less

⏱️  LATENCY:
   Textract: 4.2 minutes
   Claude: 12.5 minutes
   Difference: Textract is 8.3 min faster
```

---

## Common Issues

### "No module named 'fitz'"
```bash
pip install pymupdf
```

### "Unable to locate credentials"
Make sure `.env` file exists with valid AWS credentials

### "Model not found"
Enable Claude models in AWS Console → Bedrock → Model access

---

## Next Steps

- Try different PDFs
- Adjust parallel workers in code
- Review detailed results in S3
- See `README.md` for full documentation
