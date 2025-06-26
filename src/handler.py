from text_extractor import extract_text
from summarizer import summarize_text
from dynamo_writer import write_to_dynamodb

def process_document(file_path, table_name="DocumentSummaries"):
    """
    Full pipeline: Extract → Summarize → Write to DynamoDB
    """
    print(f"[INFO] Processing document: {file_path}")
    text = extract_text(file_path)
    if not text:
        raise ValueError("No text found in document.")

    summary = summarize_text(text)
    document_name = file_path.split("/")[-1]  # or use os.path.basename(file_path)
    write_to_dynamodb(table_name, document_name, summary)
    print(f"[SUCCESS] Summary written to DynamoDB for {document_name}")
