# Google Drive Backup Script

This script automates the process of backing up files and folders from specified Google Drive folders to a destination folder, while also deleting old backups. It utilizes Google Drive API for file operations and Discord webhooks for status updates.

## Prerequisites

Before running the script, you need to set up the following:

- Google Drive OAuth 2.0 credentials JSON file.
- Source folder IDs (Google Drive folders you want to back up).
- Destination folder ID (Google Drive folder where backups will be stored).
- Discord webhook URL for receiving status updates.

## Features

- Copies files and folders recursively from source folders to the destination folder.
- Appends the current date and time to the names of copied files and folders.
- Deletes old backups based on a specified cutoff date.
- Sends status updates to a Discord channel via webhook.

## Getting Started

1. Install the required Python dependencies listed in `requirements.txt`.

2. Configure the script:
- Set the `credentials_file` variable to the path of your Google Drive OAuth 2.0 credentials JSON file.
- Define source folder IDs, destination folder ID, and Discord webhook URL.
- Customize the schedule for running the script.

3. Run the script

4. The script will automatically copy files and folders, delete old backups, and send status updates to Discord.

## Schedule

The script is scheduled to run at specified times to perform backups and cleanup tasks. You can adjust the schedule in the script as needed. (Time and day format: HH:MM)

---

Feel free to customize and extend the script to suit your specific requirements. Please do not upload without giving credits.

---

## Setup
---

- Go to https://console.cloud.google.com
- Press `Select a Project`
<img width="402" alt="image" src="https://github.com/Clapps-lmao/Google-Copy-Bot/assets/90117687/01ea7eca-25ba-4458-8d52-399dd7ae4a29">

- Press `New Project`
- Name your project & Press Create
- Open this URL https://console.cloud.google.com/apis/library/drive.googleapis.com
- Press Enable
- Go Back to https://console.cloud.google.com/apis/dashboard
- Press `Credentials`
- Click `Create Credentials`
  <img width="348" alt="image" src="https://github.com/Clapps-lmao/Google-Copy-Bot/assets/90117687/fec9502a-b8f8-45ec-b60e-2b39da436dc0">
- Select Service Account
- Give your service account any name and click create
  <img width="681" alt="image" src="https://github.com/Clapps-lmao/Google-Copy-Bot/assets/90117687/29edc979-816a-4b36-ae3a-48434966cc86">
- Give the service account the `Owner` Role & Press Continue
- Click Done

- Edit The Service Account
- Switch to `Keys` Tab
  <img width="1137" alt="image" src="https://github.com/Clapps-lmao/Google-Copy-Bot/assets/90117687/1dfd8de8-fd89-4cbc-87da-bce1eb6ca134">

- Create New Key using `JSON` format
- Drag the json file into the same directory as your python script
- Copy the json file name and replace, after all steps completed it should look something like this.
  <img width="728" alt="image" src="https://github.com/Clapps-lmao/Google-Copy-Bot/assets/90117687/efeb46da-49da-42db-a447-6d20c1174e90">

  the rest is pretty self explanatory. Hope you all enjoy!


I AM NOT LIABLE FOR ANY DAMAGE DONE TO YOUR FILES, IF ANY.
