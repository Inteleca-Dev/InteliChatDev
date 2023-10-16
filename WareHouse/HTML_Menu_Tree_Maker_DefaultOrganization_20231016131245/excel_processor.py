'''
This file contains the ExcelProcessor class which is responsible for processing the multi-column Excel file.
'''
import pandas as pd
class ExcelProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
    def process(self):
        data = pd.read_excel(self.file_path)
        # Categorize and process the data
        processed_data = data.groupby('Category').sum()
        return processed_data