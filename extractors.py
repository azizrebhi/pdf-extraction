import fitz  # PyMuPDF
import pdfplumber
import pytesseract
import cv2
import pandas as pd
import numpy as np
from pathlib import Path
from pdf2image import convert_from_path

def extract_text_with_pymupdf(pdf_path):
    doc = fitz.open(pdf_path)
    return "".join([page.get_text() for page in doc])

def extract_tables_with_pdfplumber(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables.append(pd.DataFrame(table[1:], columns=table[0]))
    return tables

def ocr_scanned_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for img in images:
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        text += pytesseract.image_to_string(img_cv)
    return text

def save_output(text, tables, out_dir):
    Path(out_dir).mkdir(exist_ok=True)
    with open(f"{out_dir}/text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    for i, table in enumerate(tables):
        table.to_excel(f"{out_dir}/table_{i+1}.xlsx", index=False)
