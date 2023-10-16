def select_file(self):
    file_path = filedialog.askopenfilename(filetypes=[("Batch Files", "*.bat")])
    if file_path:
        self.selected_file.set(file_path)
    else:
        messagebox.showerror("Error", "No file selected!")