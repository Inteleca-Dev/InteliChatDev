# SharePoint 2019 Custom Sign-In Page User Manual

## Introduction

Welcome to the user manual for the SharePoint 2019 Custom Sign-In Page developed by ChatDev. This software allows you to create a custom sign-in page for SharePoint 2019 on-premise, which gracefully handles external logins and adjusts the authentication process to prevent repetitive login prompts. It prioritizes security and user experience to enhance your SharePoint environment.

## Installation

To install the SharePoint 2019 Custom Sign-In Page, please follow the steps below:

1. Ensure that you have the necessary dependencies installed. The required dependencies are listed in the `requirements.txt` file provided.

2. Open a command prompt or terminal and navigate to the directory where you have downloaded the SharePoint 2019 Custom Sign-In Page files.

3. Run the following command to install the necessary dependencies:

   ```
   pip install -r requirements.txt
   ```

   or

   ```
   conda install -c conda-forge --file requirements.txt
   ```

4. Once the dependencies are installed, you can proceed to configure and use the SharePoint 2019 Custom Sign-In Page.

## Configuration

To configure the SharePoint 2019 Custom Sign-In Page, please follow the steps below:

1. Open the `program.cs` file and perform any necessary initialization tasks in the `Page_Load` method.

2. Open the `signinform.cs` file and customize the sign-in form as needed. You can modify the design, add additional fields, or change the authentication logic in the `btnSignIn_Click` method.

3. If required, modify the authentication logic in the `AuthenticateUser` method to suit your specific requirements. You can check against a database or an external authentication service.

4. Customize the `signin.aspx` file to match your desired sign-in page design. You can add custom CSS styles or modify the HTML structure as needed.

## Usage

To use the SharePoint 2019 Custom Sign-In Page, please follow the steps below:

1. Ensure that you have SharePoint 2019 on-premise installed and running.

2. Deploy the SharePoint 2019 Custom Sign-In Page to your SharePoint environment. You can do this by copying the necessary files to the appropriate location.

3. Access the custom sign-in page using a web browser. The URL will depend on your SharePoint configuration and the location where you deployed the custom sign-in page.

4. Enter your username and password in the sign-in form.

5. Click the "Sign In" button to authenticate. If the authentication is successful, you will be redirected to SharePoint. Otherwise, an error message will be displayed.

## Support

If you encounter any issues or have any questions regarding the SharePoint 2019 Custom Sign-In Page, please reach out to our support team. You can contact us through our website or by filling out the support form provided.

We are committed to providing comprehensive support and ensuring that your experience with the SharePoint 2019 Custom Sign-In Page is smooth and successful.

Thank you for choosing ChatDev and the SharePoint 2019 Custom Sign-In Page!