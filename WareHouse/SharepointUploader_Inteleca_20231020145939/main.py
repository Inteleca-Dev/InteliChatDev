'''
Main script to run the SharePoint Uploader application.
'''
import tkinter as tk
from uploader import SharePointUploader
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SharePoint Uploader")
        self.geometry("400x200")
        self.uploader = SharePointUploader("http://intwsus/", "admin")
        self.create_widgets()
    def create_widgets(self):
        self.file_label = tk.Label(self, text="File Path:")
        self.file_label.pack()
        self.file_entry = tk.Entry(self)
        self.file_entry.pack()
        self.upload_button = tk.Button(self, text="Upload", command=self.upload_file)
        self.upload_button.pack()
        self.automation_var = tk.IntVar()
        self.automation_checkbox = tk.Checkbutton(self, text="Enable Automation", variable=self.automation_var)
        self.automation_checkbox.pack()
        self.schedule_button = tk.Button(self, text="Schedule", command=self.schedule_automation)
        self.schedule_button.pack()
    def upload_file(self):
        file_path = self.file_entry.get()
        self.uploader.upload_file(file_path)
    def schedule_automation(self):
        if self.automation_var.get() == 1:
            self.uploader.schedule_automation()
        else:
            self.uploader.cancel_automation()
if __name__ == "__main__":
    app = Application()
    app.mainloop()