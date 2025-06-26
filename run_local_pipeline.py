import os
import boto3
from src.text_extractor import extract_text
from src.summarizer import summarize_text
from src.dynamo_writer import write_to_dynamodb

# 🧾 Fill these in
BUCKET_NAME = "my-doc-upload-bucket"
OBJECT_KEY = "active-directory-domain-services.pdf"  # or sample.docx
TABLE_NAME = "DocumentSummaries"

def download_from_s3(bucket, key, local_path):
    s3 = boto3.client("s3")
    s3.download_file(bucket, key, local_path)

def process_file(bucket, key, table_name):
    # Step 1: Download
    import tempfile

    # At top: add
    tmpdir = tempfile.gettempdir()
    local_file = os.path.join(tmpdir, key.replace("/", "_"))

    download_from_s3(bucket, key, local_file)

    # Step 2: Extract
    print(f"[INFO] Extracting text from {local_file}")
    text = extract_text(local_file)
    if not text:
        raise ValueError("No extractable text found.")

    # Step 3: Summarize
    print("[INFO] Summarizing...")
    summary = summarize_text(text)

    # Step 4: Store
    print("[INFO] Writing to DynamoDB...")
    write_to_dynamodb(table_name, key, summary)

    print("\nSummary written to DynamoDB!")
    print("\n--- Summary Preview ---\n")
    print(summary)

if __name__ == "__main__":
    process_file(BUCKET_NAME, OBJECT_KEY, TABLE_NAME)
