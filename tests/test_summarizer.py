import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from summarizer import summarize_text

def test_summarize_short_text():
    text = (
        "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. "
        "It is named after the engineer Gustave Eiffel, whose company designed and built the tower. "
        "Constructed from 1887 to 1889, it was the entrance arch to the 1889 World's Fair."
    )
    summary = summarize_text(text)
    assert isinstance(summary, str)
    assert len(summary) < len(text)
