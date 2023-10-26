'''
Module for SharePointUploader class to handle file upload and automation.
'''
import os
import schedule
import time
class SharePointUploader:
    def __init__(self, servername, username):
        self.servername = servername
        self.username = username
        self.automation_scheduled = False
    def upload_file(self, file_path):
        if os.path.exists(file_path):
            # Logic to upload the file to SharePoint using the servername and username
            print(f"Uploading file: {file_path}")
        else:
            print("File not found.")
    def enable_automation(self):
        # Logic to enable automations
        print("Automation enabled.")
    def disable_automation(self):
        # Logic to disable automations
        print("Automation disabled.")
    def schedule_automation(self):
        if not self.automation_scheduled:
            schedule.every().day.at("09:00").do(self.enable_automation)
            self.automation_scheduled = True
            print("Automation scheduled.")
        else:
            print("Automation already scheduled.")
    def cancel_automation(self):
        if self.automation_scheduled:
            schedule.clear()
            self.automation_scheduled = False
            print("Automation canceled.")
        else:
            print("No automation scheduled.")
    def run_scheduled_automations(self):
        while True:
            schedule.run_pending()
            time.sleep(1)