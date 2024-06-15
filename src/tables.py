"""Use it if you need to parse some table"""
"""In my case I'm using table 3C for Costal discharged Water."""

from img2table.document import PDF
from img2table.ocr import TesseractOCR
import os

def get_table(pdf_file, page_number):
    pdf_file = os.path.join(os.getcwd(), "files", pdf_file)

    pdf = PDF(src=pdf_file, pages=[page_number])

    ocr = TesseractOCR(lang="eng")
    pdf_tables = pdf.extract_tables(ocr=ocr,
                                    implicit_rows=True,
                                    borderless_tables=False,
                                    min_confidence=50)

    output_file = f"{pdf_file}_{page_number}.xlsx"
    output_path = os.path.join(os.getcwd(), "files", output_file)
 
    pdf.to_xlsx(output_path)

