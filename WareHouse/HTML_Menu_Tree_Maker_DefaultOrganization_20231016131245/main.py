'''
This is the main file of the Python application. It handles the user interface and coordinates the processing of the Excel file.
'''
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from excel_processor import ExcelProcessor
from html_generator import HTMLGenerator
from css_generator import CSSGenerator
from js_generator import JSGenerator
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Excel Processor")
        self.geometry("400x200")
        self.file_path = None
        self.select_file_button = tk.Button(self, text="Select Excel File", command=self.select_file)
        self.select_file_button.pack(pady=10)
        self.process_button = tk.Button(self, text="Process File", command=self.process_file)
        self.process_button.pack(pady=10)
    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    def process_file(self):
        if self.file_path:
            excel_processor = ExcelProcessor(self.file_path)
            data = excel_processor.process()
            html_generator = HTMLGenerator()
            html_content = html_generator.generate(data)
            html_generator.save_html(html_content)
            css_generator = CSSGenerator()
            css_content = css_generator.generate()
            css_generator.save_css(css_content)
            js_generator = JSGenerator()
            js_content = js_generator.generate()
            js_generator.save_js(js_content)
            # Additional code to integrate with existing application structure
            # Show success message to the user
            messagebox.showinfo("Success", "File processed successfully!")
        else:
            # Show error message to the user
            messagebox.showerror("Error", "No file selected!")
if __name__ == "__main__":
    app = Application()
    app.mainloop()