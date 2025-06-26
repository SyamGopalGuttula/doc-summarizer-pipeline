from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Use a small model to fit within Lambda ZIP limits
tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
summarizer_pipeline = pipeline("summarization", model=model, tokenizer=tokenizer)

def summarize_text(text, max_chunk_length=512):
    chunks = split_text(text, max_chunk_length)
    summaries = []
    for chunk in chunks:
        result = summarizer_pipeline(chunk, max_length=100, min_length=30, do_sample=False)
        summaries.append(result[0]['summary_text'])
    return "\n\n".join(summaries)

def split_text(text, max_tokens):
    import re
    sentences = re.split(r'(?<=[.?!])\s+', text)
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_tokens:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks
