import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from text_extractor import extract_text

def test_extract_text_from_pdf():
    file_path = "tests/sample.pdf"  # must exist
    text = extract_text(file_path)
    assert isinstance(text, str)
    assert len(text) > 10

def test_extract_text_from_docx():
    file_path = "tests/sample.docx"  # must exist
    text = extract_text(file_path)
    assert isinstance(text, str)
    assert len(text) > 10
