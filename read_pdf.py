import sys
import subprocess
import os

# Try to use pdfminer if available, otherwise use a basic approach
try:
    from pdfminer.high_level import extract_text
    text = extract_text(r'C:\Users\pc\.openclaw\workspace\indonesia_law.pdf')
    print(text)
except ImportError:
    # Try with PyPDF2
    try:
        import PyPDF2
        with open(r'C:\Users\pc\.openclaw\workspace\indonesia_law.pdf', 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                print(page.extract_text())
    except ImportError:
        print("No PDF library available")
        sys.exit(1)
