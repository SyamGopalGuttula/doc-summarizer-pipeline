import os
import boto3
import tempfile
from src.text_extractor import extract_text
from src.summarizer import summarize_text
from src.dynamo_writer import write_to_dynamodb

s3 = boto3.client("s3")

def lambda_handler(event, context):
    # Get S3 bucket and file info
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    # Download file to temp location
    with tempfile.TemporaryDirectory() as tmpdir:
        download_path = os.path.join(tmpdir, key.split("/")[-1])
        s3.download_file(bucket, key, download_path)

        # Process
        text = extract_text(download_path)
        if not text:
            raise ValueError("No extractable text in file.")

        summary = summarize_text(text)
        write_to_dynamodb("DocumentSummaries", key, summary)

    return {"statusCode": 200, "body": "Document summarized successfully"}
