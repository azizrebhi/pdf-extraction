import streamlit as st
import tempfile
import pandas as pd
from extractors import extract_text_with_pymupdf, extract_tables_with_pdfplumber, ocr_scanned_pdf

st.set_page_config(page_title="PDF Extractor", layout="wide")
st.title("📄 PDF Text & Table Extractor")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.info("Extracting text...")
    text = extract_text_with_pymupdf(tmp_path)

    st.info("Extracting tables...")
    tables = extract_tables_with_pdfplumber(tmp_path)

    if len(text.strip()) < 100:
        st.warning("Low text detected. Running OCR...")
        text = ocr_scanned_pdf(tmp_path)

    st.subheader("📜 Extracted Text")
    st.text_area("Text Output", text, height=300)
    st.download_button("📥 Download Text", text, file_name="text.txt")

    st.subheader("📊 Extracted Tables")
    if tables:
        for i, table in enumerate(tables):
            st.markdown(f"**Table {i+1}**")
            st.dataframe(table)
            csv = table.to_csv(index=False).encode("utf-8")
            st.download_button(f"Download Table {i+1}", csv, file_name=f"table_{i+1}.csv")
    else:
        st.info("No tables found in PDF.")
