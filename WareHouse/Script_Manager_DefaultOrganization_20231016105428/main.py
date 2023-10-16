'''
This is the main file of the application. It contains the GUI implementation using the tkinter framework and handles the scheduling of .bat files and logging the execution details to a SQL file.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import subprocess
import datetime
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Batch File Scheduler")
        self.geometry("400x300")
        self.selected_file = tk.StringVar()
        self.schedule_time = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        file_label = tk.Label(self, text="Select .bat file:")
        file_label.pack()
        file_button = tk.Button(self, text="Browse", command=self.select_file)
        file_button.pack()
        time_label = tk.Label(self, text="Select schedule time (HH:MM):")
        time_label.pack()
        time_entry = tk.Entry(self, textvariable=self.schedule_time)
        time_entry.pack()
        schedule_button = tk.Button(self, text="Schedule", command=self.schedule)
        schedule_button.pack()
    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Batch Files", "*.bat")])
        if file_path:
            self.selected_file.set(file_path)
        else:
            messagebox.showerror("Error", "No file selected!")
    def schedule(self):
        file_path = self.selected_file.get()
        schedule_time = self.schedule_time.get()
        if file_path and schedule_time:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if schedule_time < current_time:
                messagebox.showerror("Error", "Schedule time cannot be in the past!")
            else:
                try:
                    subprocess.Popen(["schtasks", "/create", "/tn", "BatchFileTask", "/tr", file_path, "/sc", "once", "/st", schedule_time])
                    self.log_execution(file_path, schedule_time)
                    messagebox.showinfo("Success", "Batch file scheduled successfully!")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select a file and schedule time!")
    def log_execution(self, file_path, schedule_time):
        conn = sqlite3.connect("execution_logs.db")
        cursor = conn.cursor()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO logs (file_path, schedule_time, execution_time) VALUES (?, ?, ?)",
                       (file_path, schedule_time, current_time))
        conn.commit()
        conn.close()
if __name__ == "__main__":
    app = Application()
    app.mainloop()