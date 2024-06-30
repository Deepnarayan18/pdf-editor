import customtkinter as ctk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()
    
    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def split_pdf(path, output_folder):
    pdf_reader = PdfFileReader(path)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page))
        
        output_filename = f'{output_folder}/page_{page + 1}.pdf'
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

def rotate_pdf(input_pdf, output_pdf, rotation):
    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()
    
    for page in pdf_reader.pages:
        pdf_writer.addPage(page.rotateClockwise(rotation))
    
    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def open_files_dialog():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    return file_paths

def save_file_dialog():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    return file_path

def save_folder_dialog():
    folder_path = filedialog.askdirectory()
    return folder_path

def merge_action():
    files = open_files_dialog()
    if files:
        output_path = save_file_dialog()
        if output_path:
            merge_pdfs(files, output_path)
            messagebox.showinfo("Success", "PDFs merged successfully!")

def split_action():
    file = open_file_dialog()
    if file:
        output_folder = save_folder_dialog()
        if output_folder:
            split_pdf(file, output_folder)
            messagebox.showinfo("Success", "PDF split successfully!")

def rotate_action():
    file = open_file_dialog()
    if file:
        output_path = save_file_dialog()
        if output_path:
            rotate_pdf(file, output_path, 90)  # Rotate by 90 degrees
            messagebox.showinfo("Success", "PDF rotated successfully!")

# CustomTkinter GUI setup
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("PDF Editor")

# Card setup
card_frame = ctk.CTkFrame(master=root, corner_radius=15)
card_frame.pack(pady=20, padx=30, fill="both", expand=True)

label = ctk.CTkLabel(master=card_frame, text="PDF Editor", font=("Arial", 24))
label.pack(pady=12, padx=10)

merge_button = ctk.CTkButton(master=card_frame, text="Merge PDFs", command=merge_action)
merge_button.pack(pady=10)

split_button = ctk.CTkButton(master=card_frame, text="Split PDF", command=split_action)
split_button.pack(pady=10)

rotate_button = ctk.CTkButton(master=card_frame, text="Rotate PDF", command=rotate_action)
rotate_button.pack(pady=10)

root.mainloop()
