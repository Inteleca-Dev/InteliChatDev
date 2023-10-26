'''
This module processes the Excel file and categorizes the data.
'''
import pandas as pd
def process_excel(df):
    # Categorize the data
    categorized_data = df.groupby('Category').apply(lambda x: x.to_dict('records')).to_dict()
    return categorized_data