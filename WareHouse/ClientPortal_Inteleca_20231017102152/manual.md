# Client Portal

A web application that allows for secure login and data display from an in-house Microsoft SQL Server. The application also supports data export to Excel.

## Quick Install

To install the necessary dependencies, run the following command in your terminal:

`pip install pyodbc pandas bcrypt getpass`

## What is this?

This application is designed to provide a secure portal for clients to access and export their data stored in an in-house Microsoft SQL Server. The application is built using Python and leverages several libraries to handle database connection, user authentication, and data export.

Key features of the application include:

**Secure Login:** The application uses bcrypt for password hashing and secure user authentication.

**Data Display:** Once logged in, the client can view their data fetched directly from the SQL Server.

**Excel Export:** The application supports exporting the displayed data to an Excel file.

## Documentation

Please follow the steps below to use the application:

1. **Install Dependencies:** Ensure that all necessary Python libraries are installed. You can do this by running the command mentioned in the Quick Install section.

2. **Set Up Database Connection:** In the `database.py` file, replace `server_name` and `db_name` with your actual SQL Server details.

3. **Run the Application:** Execute the `main.py` file to start the application. This will prompt you to enter your username and password.

4. **Login:** Enter your username and password. If the entered credentials are correct, the application will fetch and display your data.

5. **Export Data:** The application will automatically export your data to an Excel file named `data.xlsx`.

Please note that the application assumes the existence of a 'users' table in the SQL Server database with fields for 'username', 'password', and 'user_id'. The password should be stored as a bcrypt hash.