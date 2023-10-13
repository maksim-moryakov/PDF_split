import tkinter as tk
from tkinter import filedialog
import PyPDF2


def select_file():
    global file_path
    file_path = filedialog.askopenfilename()

def get_file_path():
    global steps
    steps = page_entry.get()
    

def extract_pages():
    output_prefix = 'extracted_pages'
    start_page = 1
    step = int(steps)
    with open(file_path, 'rb') as file:
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



def create_ui():
    root = tk.Tk()
    root.title("Приложение для разделения PDF")
    root.geometry("400x400")

    # Создание кнопки для выбора файла
    file_button = tk.Button(root, text="Нажми для выбора файла для разделения", command=select_file)
    file_button.pack(expand=True, ipadx=10, ipady=10)

    # Создание поля для ввода количества страниц
    page_label = tk.Label(root, text="Введите по сколько страниц надо разделить файл:")
    page_label.pack()
    global page_entry
    page_entry = tk.Entry(root)
    page_entry.pack()

    # Создание кнопки для получения значения из текстового поля
    button = tk.Button(root, text="Подтвердить введеное значение", command=get_file_path)
    button.pack()

    # Создание кнопки для запуска извлечения страниц
    extract_button = tk.Button(root, text="Разделить файл", command=extract_pages)
    extract_button.pack(expand=True, ipadx=20, ipady=20)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
