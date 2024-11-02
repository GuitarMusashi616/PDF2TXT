import sys
import os
try:
    from PyPDF2 import PdfReader
except ImportError:
    print("PyPDF2 module not found. Install it using 'pip install PyPDF2'")
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: py pdf2txt.py filename.pdf")
        sys.exit(1)
        
    pdf_file = sys.argv[1]

    if not os.path.isfile(pdf_file):
        print(f"Error: File '{pdf_file}' does not exist.")
        sys.exit(1)
    if not pdf_file.lower().endswith('.pdf'):
        print(f"Error: File '{pdf_file}' is not a PDF file.")
        sys.exit(1)

    txt_file = os.path.splitext(pdf_file)[0] + '.txt'

    try:
        reader = PdfReader(pdf_file)
        with open(txt_file, 'w', encoding='utf-8') as f_out:
            for page_number, page in enumerate(reader.pages, start=1):
                text = page.extract_text()
                if text:
                    f_out.write(f"--- Page {page_number} ---\n")
                    f_out.write(text)
                    f_out.write("\n\n")
            print(f"Text extracted to '{txt_file}' with page numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
