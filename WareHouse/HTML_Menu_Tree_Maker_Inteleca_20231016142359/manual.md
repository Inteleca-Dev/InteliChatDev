# Python Excel Processor

This Python application processes a multi-column Excel file, categorizes data, and generates a folder with the HTML and CSS file that opens the Excel file and creates a nested menu.

## Quick Install

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Main Features

1. **Excel Processing**: The application reads an Excel file and categorizes the data based on the 'Category' column.

2. **HTML and CSS Generation**: The application generates an HTML file using the categorized data. The HTML file is styled using CSS.

3. **Nested Menu Creation**: The application creates a nested menu using the categorized data. The menu is displayed in a new window.

## How to Use

1. **Prepare Your Excel File**: Make sure your Excel file has a 'Category' column. The application will categorize the data based on this column.

2. **Run the Application**: Run the `main.py` file. The application will read the Excel file, categorize the data, generate the HTML and CSS files, and create the nested menu.

3. **View the Results**: After running the application, you can view the generated HTML file in your browser. You can also interact with the nested menu in the new window that opens.

## Documentation

For more detailed information on how to use this application, please refer to the following files:

- `main.py`: This is the main entry point of the application. It calls all the functions in the correct order to accomplish the task.

- `excel_processor.py`: This module processes the Excel file and categorizes the data.

- `html_css_generator.py`: This module generates the HTML and CSS files based on the categorized data.

- `menu_creator.py`: This module creates a nested menu based on the categorized data.

- `requirements.txt`: This file lists the Python packages that your project depends on. You should use pip to install these dependencies.

For any additional support or queries, please contact our support team.