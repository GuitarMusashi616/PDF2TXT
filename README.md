# PDF to Text Converter

**Easily convert PDF documents to text files with page numbers included.**

---

## Introduction

`pdf2txt.py` is a simple yet powerful Python script designed to extract text from PDF files and save it into a `.txt` file. It not only converts the PDF content but also annotates each page with its corresponding page number, making it easier to reference and navigate through large text files.

---

## Features

- **Simple Command-Line Interface**: Convert PDFs to text using a single command.
- **Page Numbering**: Automatically includes page numbers in the output text file.
- **Robust Error Handling**: Checks for file existence, correct file extensions, and handles exceptions gracefully.
- **Unicode Support**: Handles text encoding to support a wide range of characters.

---

## Prerequisites

- **Python 3.x**: Make sure you have Python installed on your system.
- **PyPDF2 Library**: A Python library for PDF file handling.

---

## Installation

Install the required library using pip:

```bash
pip install PyPDF2
```

## Usage

Open your command prompt or terminal, navigate to the directory containing pdf2txt.py, and run:

```bash
python pdf2txt.py filename.pdf
```

