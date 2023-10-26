'''
This is the main entry point of the application. It calls all the functions in the correct order to accomplish the task.
'''
import pandas as pd
from excel_processor import process_excel
from html_css_generator import generate_html_css
from menu_creator import create_menu
def main():
    # Load the Excel file
    df = pd.read_excel('C:\GitHub\InteliChatDev\WareHouse\HTML_Menu_Tree_Maker_Inteleca_20231016142359\Shopify-Categories.xlsx') # Updated the file path to the correct location
    # Process the Excel file and categorize the data
    categorized_data = process_excel(df)
    # Generate the HTML and CSS files
    generate_html_css(categorized_data)
    # Create the nested menu
    create_menu(categorized_data)
if __name__ == "__main__":
    main()