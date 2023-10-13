import PyPDF2
import tkinter as tk
from tkinter import filedialog

def extract_pages(input_path, output_prefix, start_page, step):
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        num_pages = len(reader.pages)
        current_page = start_page - 1

        while current_page < num_pages:
            writer = PyPDF2.PdfWriter()

            for page_number in range(current_page, min(current_page + step, num_pages)):
                page = reader.pages[page_number]
                writer.add_page(page)

            output_file = f"{output_prefix}_{current_page + 1}-{min(current_page + step, num_pages)}.pdf"
            with open(output_file, 'wb') as output_file:
                writer.write(output_file)

            current_page += step

            

# Пример использования
input_file = 'DOC.pdf'
output_prefix = 'extracted_pages'
start_page = 1
step = 8

extract_pages(input_file, output_prefix, start_page, step)