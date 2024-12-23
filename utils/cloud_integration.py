from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import io

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.file']


class GoogleDriveIntegration:
    def __init__(self, credentials_file='credentials.json', token_file='token.json'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.service = None

    def authenticate(self):
        creds = None
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())
        self.service = build('drive', 'v3', credentials=creds)

    def upload_file(self, file_path, folder_id=None):
        try:
            if not self.service:
                self.authenticate()
            file_metadata = {'name': os.path.basename(file_path)}
            if folder_id:
                file_metadata['parents'] = [folder_id]
            media = MediaFileUpload(file_path, resumable=True)
            file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f'File ID: {file.get("id")} uploaded.')
            return file.get('id')
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None

    def download_file(self, file_id, file_path):
        try:
            if not self.service:
                self.authenticate()
            request = self.service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(f'Download {int(status.progress() * 100)}%.')
            with open(file_path, 'wb') as f:
                f.write(fh.getvalue())
            return file_path
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None

    def list_files_in_folder(self, folder_id):
        try:
            if not self.service:
                self.authenticate()
            results = self.service.files().list(
                q=f"'{folder_id}' in parents",
                fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])
            return items
        except HttpError as error:
            print(f'An error occurred: {error}')
            return []

    def get_file_name(self, file_id):
        try:
            if not self.service:
                self.authenticate()
            file = self.service.files().get(fileId=file_id).execute()
            return file.get('name')
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None
