# pyright: strict

import sys
from pathlib import Path
import PyPDF2

def extract_pdf_to_text(pdf_path: str, output_text_file: str, include_page_numbers: bool = False) -> None:
    try:
        with open(pdf_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Open a text file to write the extracted text
            with open(output_text_file, 'w', encoding='utf-8') as text_file:
                # Iterate through all the pages and extract text
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()

                    if not text:
                        continue

                    if include_page_numbers:
                        text_file.write(f"--- Page {page_num + 1} ---\n")

                    # Write the extracted text to the text file
                    text_file.write(text)
                    text_file.write("\n")

        print(f"Text extracted and saved to {output_text_file}")
    except Exception as e:
        print(f"Error processing file: {e}")


def main():
    if len(sys.argv) not in {2, 3}:
        print("Usage: python pdf2txt.py <input_pdf_file>")
        print("Example: python pdf2txt.py something.pdf (outputs to something.txt)")
        print("Usage: python pdf2txt.py <input_pdf_dir> [output_txt_dir]")

    if len(sys.argv) == 2:
        pdf_path = Path(sys.argv[1])

        if not pdf_path.exists():
            print("Error: Source path is not valid.")
        
        if pdf_path.is_file():
            output_txt_path = pdf_path.with_suffix('.txt')
            extract_pdf_to_text(str(pdf_path), str(output_txt_path))

        if pdf_path.is_dir():
            for pdf_file in pdf_path.iterdir():
                if not pdf_file.suffix == '.pdf':
                    continue

                output_txt_path = pdf_path.with_suffix('.txt')
                extract_pdf_to_text(str(pdf_file), str(output_txt_path))

    else:
        pdf_path = Path(sys.argv[1])
        txt_path = Path(sys.argv[2])

        if not pdf_path.exists() or pdf_path.is_file():
            print("Error: Source path is not valid.")

        if txt_path.exists() and txt_path.is_file():
            print("Error: Destination path is not valid.")

        if not txt_path.exists():
            txt_path.mkdir(711)

        for pdf_file in pdf_path.iterdir():
            if not pdf_file.suffix == '.pdf':
                continue

            output_txt_path = txt_path / pdf_path.with_suffix('.txt').name
            extract_pdf_to_text(str(pdf_file), str(output_txt_path))

# Entry point of the script
if __name__ == "__main__":
    main()