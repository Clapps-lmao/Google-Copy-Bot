import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from discord_webhook import DiscordWebhook
import schedule
import time
import datetime

# Set your Google Drive credentials
credentials_file = 'json-file'

# Set your source folder IDs and destination folder ID
source_folder_ids = [
    'folders-you-want-to-copy-from',
]
destination_folder_id = 'folder-you-want-to-copy-into'

# Set your Discord webhook URL
discord_webhook_url = 'enter-your-webhook-here'

creds = None

if os.path.exists(credentials_file):
    creds = service_account.Credentials.from_service_account_file(credentials_file, scopes=['https://www.googleapis.com/auth/drive'])
else:
    print(f"Credentials file '{credentials_file}' not found. Please provide the path to your credentials JSON file.")
    exit()

drive_service = build('drive', 'v3', credentials=creds)


def delete_old_backups():
    try:
        cutoff_date = datetime.datetime.now() - datetime.timedelta(hours=12)
        cutoff_date_str = cutoff_date.strftime('%Y-%m-%d')
        q = f"'{destination_folder_id}' in parents"
        results = drive_service.files().list(q=q).execute()
        files = results.get('files', [])
        for file in files:
            if file['name'].startswith('backup-') and file['name'].endswith(cutoff_date_str):
                drive_service.files().delete(fileId=file['id']).execute()
                print(f"Old backup '{file['name']}' deleted.")

    except Exception as e:
        send_discord_error_message(f"Error deleting old backups: {str(e)}")
        print(f"Error deleting old backups: {str(e)}")
def copy_files_and_folders(source_folder_id, destination_folder_id):
    try:
        copied_file_names = [] 
        current_datetime = datetime.datetime.now()
        current_datetime_str = current_datetime.strftime('%Y-%m-%d-%H-%M-%S')
        q = f"'{source_folder_id}' in parents"
        results = drive_service.files().list(q=q).execute()
        items = results.get('files', [])
        for item in items:
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                folder_name = item['name']
                folder_metadata = {'name': f'backup-{folder_name}-{current_datetime_str}', 'parents': [destination_folder_id], 'mimeType': 'application/vnd.google-apps.folder'}
                new_folder = drive_service.files().create(body=folder_metadata).execute()
                copy_files_and_folders(item['id'], new_folder['id'])  
            else:
                file_name = item['name']
                file_metadata = {'name': f'backup-{file_name}-{current_datetime_str}', 'parents': [destination_folder_id]}
                response = drive_service.files().copy(fileId=item['id'], body=file_metadata, supportsAllDrives=True).execute()
                copied_file_names.append(f"'{file_name}' copied to '{destination_folder_id}' with new name '{response['name']}'")

        if copied_file_names:
            send_discord_success_message(copied_file_names, folder_name)  
            print("Files and folders copied successfully.")
        else:
            send_discord_success_message([], folder_name) 
            print(f"No files were copied from folder '{folder_name}'.")
    except Exception as e:
        send_discord_error_message(f"Error copying files and folders: ``{str(e)}")
        print(f"Error copying files and folders: ``{str(e)}``")
def send_discord_success_message(copied_file_names, folder_name):
    if copied_file_names:
        message = f"Files copied successfully from folder '{folder_name}':\n" + "\n".join(copied_file_names)
    else:
        message = f"No files were copied from folder '{folder_name}'."
    webhook = DiscordWebhook(url=discord_webhook_url, content=message)
    webhook.execute()
def send_discord_error_message(error_message):
    message = f"Error: ``{error_message}``"
    webhook = DiscordWebhook(url=discord_webhook_url, content=message)
    webhook.execute()

schedule.every().day.at("23:50").do(delete_old_backups)
schedule.every().day.at("0:00").do(lambda: copy_files_and_folders(source_folder_ids[0], destination_folder_id))

while True:
    schedule.run_pending()
    time.sleep(1)
