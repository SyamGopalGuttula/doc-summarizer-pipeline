# 📄 Document Summarizer Pipeline (Local & Serverless-ready)

This project summarizes text content from PDF, DOCX, and TXT files using a free, local Hugging Face model (`t5-small`). It supports both local runs and packaging for AWS Lambda (via Docker).

---

## 🧰 Features

- ✅ Text extraction from PDF and DOCX
- ✅ Summarization using a compact Transformers model
- ✅ Manual run on local files or S3 bucket contents
- ✅ Docker-based build for Lambda Layer packaging (Torch + Transformers)

---

## 🏗️ Project Structure

```
doc-summarizer-pipeline/
├── extractor/
│   ├── pdf_extractor.py
│   └── docx_extractor.py
├── summarizer.py
├── dynamodb_writer.py
├── run_local_pipeline.py
├── lambda_function.py
├── requirements.txt
├── requirements-docker.txt
├── Dockerfile
├── .dockerignore
└── tests/
```

---

## 🧪 Testing

Use `pytest` to test extractors, summarizer, and DynamoDB writer.

```bash
pytest tests/
```

---

## 🐳 Build Lambda Layer with Docker (Optional)

To bundle `transformers`, `torch`, and `sentencepiece` into a Lambda-compatible layer:

```bash
# Build image
docker build -t lambda-layer-builder .

# Copy zip from container to host
docker run --rm -v "%cd%:/lambda" --entrypoint /bin/bash lambda-layer-builder -c "cp /lambda/lambda-layer.zip /lambda/"
```

---

## 🚀 Local Usage

You can test the pipeline manually with:

```bash
python run_local_pipeline.py
```

---

Let me know if you'd like to add deployment steps, S3 trigger setup, or layer publishing instructions.

