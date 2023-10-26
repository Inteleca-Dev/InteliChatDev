'''
This file handles the export of data to Excel.
'''
import pandas as pd
def to_excel(data):
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    # Export to Excel
    df.to_excel('data.xlsx', index=False)