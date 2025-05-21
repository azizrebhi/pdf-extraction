# PDF Text & Table Extractor

A user-friendly web application built with **Streamlit** to extract text and tables from PDF documents. This tool supports both digitally generated PDFs and scanned/image-based PDFs through integrated OCR (Optical Character Recognition).

---

## Features

- Extract selectable text from PDFs using **PyMuPDF**
- Detect and extract tables as pandas DataFrames using **pdfplumber**
- Automatically runs OCR via **Tesseract** on scanned PDFs for text extraction
- Interactive web interface with file upload and instant preview of extracted content
- Download extracted text as `.txt` and tables as `.csv` files
- Simple and easy-to-use — no coding required

---

## Demo

Run the app locally or deploy it on platforms like [Streamlit Cloud](https://streamlit.io/cloud) or Heroku to share with others.

---

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/azizrebhi/pdf-extraction.git
    cd pdf-extraction
    ```

2. Create and activate a virtual environment (recommended):

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Install system dependencies:

    - **Tesseract OCR engine**  
      Follow the installation instructions:  
      https://github.com/tesseract-ocr/tesseract#installation

    - **Poppler** (required by pdf2image)  
      Follow the installation instructions:  
      https://pdf2image.readthedocs.io/en/latest/installation.html

---

## Usage

Start the app with:

```bash
streamlit run app.py
