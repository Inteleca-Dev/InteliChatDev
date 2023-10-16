# Batch File Scheduler User Manual

## Introduction

The Batch File Scheduler is a Python tkinter application that allows you to schedule the execution of .bat files and record the execution logs in a SQL file for review. This user manual will guide you on how to install the necessary dependencies and use the application effectively.

## Installation

To use the Batch File Scheduler, you need to install the following dependencies:

- Python (version 3.6 or higher)
- tkinter
- sqlite3

You can install these dependencies by running the following command:

```
pip install -r requirements.txt
```

## Usage

1. Run the `main.py` file to start the application.

2. The application window will open with the title "Batch File Scheduler" and a size of 400x300.

3. Select a .bat file by clicking the "Browse" button. This will open a file dialog where you can navigate to the desired .bat file and select it.

4. Enter the schedule time in the format HH:MM in the text field next to the "Select schedule time" label.

5. Click the "Schedule" button to schedule the execution of the selected .bat file at the specified time.

6. If the schedule time is in the past, an error message will be displayed. Otherwise, the .bat file will be scheduled using the `schtasks` command and the execution details will be logged to the SQL file.

7. If the scheduling and logging are successful, a success message will be displayed. Otherwise, an error message will be displayed.

8. You can review the execution logs by opening the `execution_logs.db` file. The logs are stored in the "logs" table, which has the following columns: id, file_path, schedule_time, and execution_time.

## Example

Let's walk through an example to schedule the execution of a .bat file using the Batch File Scheduler:

1. Run the `main.py` file.

2. Click the "Browse" button and select a .bat file from your computer.

3. Enter the schedule time in the format HH:MM, e.g., 09:30.

4. Click the "Schedule" button.

5. If the scheduling and logging are successful, a success message will be displayed.

6. Open the `execution_logs.db` file to review the execution logs.

## Conclusion

The Batch File Scheduler is a useful tool for scheduling the execution of .bat files and recording the execution logs for review. By following the instructions in this user manual, you can easily install the necessary dependencies and use the application effectively. If you have any further questions or issues, please reach out to our support team for assistance.