import argparse
from extractors import extract_text_with_pymupdf, extract_tables_with_pdfplumber, ocr_scanned_pdf, save_output

def main():
    parser = argparse.ArgumentParser(description="Extract content from PDF")
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("--out", default="output", help="Output directory")
    args = parser.parse_args()

    print("Extracting text with PyMuPDF...")
    text = extract_text_with_pymupdf(args.pdf_path)

    print("Extracting tables with pdfplumber...")
    tables = extract_tables_with_pdfplumber(args.pdf_path)

    if len(text.strip()) < 100:
        print("Low text detected — running OCR...")
        text = ocr_scanned_pdf(args.pdf_path)

    save_output(text, tables, args.out)
    print(f"Extraction complete. Results saved to '{args.out}'.")

if __name__ == "__main__":
    main()
