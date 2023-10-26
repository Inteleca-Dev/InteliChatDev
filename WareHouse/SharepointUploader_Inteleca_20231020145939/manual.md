# SharePoint Uploader User Manual

## Introduction

The SharePoint Uploader is a Python application that allows you to upload files into an onsite SharePoint using Python. It provides the ability to toggle automations and schedule when they should run. This user manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to use it.

## Installation

To use the SharePoint Uploader, you need to install the required dependencies. Follow the steps below to install the necessary packages:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt and navigate to the directory where you have downloaded the SharePoint Uploader files.

3. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   This will install the `schedule` package, which is used for scheduling automations.

## Usage

Once you have installed the dependencies, you can start using the SharePoint Uploader. Follow the steps below to use the main functions of the software:

1. Open a terminal or command prompt and navigate to the directory where you have downloaded the SharePoint Uploader files.

2. Run the following command to start the application:

   ```
   python main.py
   ```

   This will open the SharePoint Uploader application window.

3. In the application window, you will see a file path input field and an upload button. Enter the path of the file you want to upload into the SharePoint in the file path input field.

4. Click the upload button to upload the file to the SharePoint. The application will display a message indicating whether the file was successfully uploaded or if any errors occurred.

5. To toggle automations, you can enable or disable the automation checkbox in the application window. When the automation is enabled, the SharePoint Uploader will perform certain actions automatically based on the schedule.

6. To schedule automations, click the schedule button in the application window. This will schedule the automation to run at 09:00 every day. If the automation is already scheduled, a message will be displayed indicating that it is already scheduled.

7. To cancel the scheduled automation, click the schedule button again. This will cancel the automation schedule. If no automation is scheduled, a message will be displayed indicating that no automation is scheduled.

8. If you want to run the scheduled automations, you can use the `run_scheduled_automations` function in the `uploader.py` module. This function will continuously check for pending automations and execute them when the scheduled time arrives.

## Conclusion

The SharePoint Uploader provides a simple and convenient way to upload files into an onsite SharePoint using Python. With the ability to toggle automations and schedule when they should run, you can automate repetitive tasks and improve your productivity. Follow the instructions in this user manual to install and use the SharePoint Uploader effectively. If you have any questions or encounter any issues, please refer to the documentation or contact our support team for assistance.