# Custom Sign-In Page for SharePoint 2019 On-Premise

## Introduction

The Custom Sign-In Page for SharePoint 2019 On-Premise is a Python-based web application that provides a customized sign-in experience for external users accessing SharePoint 2019 on-premise. It detects external access and adjusts the authentication process to prevent repetitive login prompts, ensuring both security and user experience are prioritized.

## Installation

To install the Custom Sign-In Page, follow these steps:

1. Ensure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone the repository or download the source code files to your local machine.

3. Open a terminal or command prompt and navigate to the directory where the source code files are located.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment by running the appropriate command based on your operating system:

   - Windows:

     ```
     venv\Scripts\activate
     ```

   - macOS/Linux:

     ```
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Custom Sign-In Page, follow these steps:

1. Ensure you have completed the installation steps mentioned above.

2. Open a terminal or command prompt and navigate to the directory where the source code files are located.

3. Run the following command to start the application:

   ```
   python main.py
   ```

4. The application will launch a window with a sign-in form.

5. Enter your username in the provided field and click the "Sign In" button.

6. The application will perform the authentication logic and adjust the authentication process if external access is detected.

7. If external access is detected, the application will generate a token for the user, store it, and authenticate the user using the token.

8. If external access is not detected, the application will proceed with the regular authentication process.

## Customization

The Custom Sign-In Page can be customized to fit your specific requirements. Here are some areas you can consider customizing:

- User Interface: You can modify the sign-in form layout, add additional fields, or enhance the visual design using the Tkinter library.

- Authentication Logic: The `sign_in` method in the `SignInPage` class is where the authentication logic is implemented. You can customize this method to integrate with your existing authentication system or add additional security checks.

- Token-based Authentication: The `adjust_authentication_process` method in the `SignInPage` class demonstrates a sample implementation of token-based authentication. You can modify this method to use a different authentication mechanism if needed.

## Conclusion

The Custom Sign-In Page for SharePoint 2019 On-Premise provides a solution for gracefully handling external logins and improving the authentication process for external users. By following the installation and usage instructions, you can easily integrate this custom sign-in page into your SharePoint 2019 on-premise environment.