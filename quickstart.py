from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    creds = None
    # Check if the token.json file exists (stores user's access and refresh tokens)
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If no valid credentials are available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=8000)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    # Create a service object to interact with the Gmail API
    service = build('gmail', 'v1', credentials=creds)

    # Get the user's inbox messages
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=1).execute()
    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')
    else:
        print('Messages:')
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            headers = msg.get('payload', {}).get('headers', [])
            print(headers)
            # cleanMsg = convertToJson(msg)
            # print(cleanMsg)

# def convertToJson(msg):
#     headers = msg.get('payload', {}).get('headers', [])
#     if headers['name'] == 'From':
#         return headers['value']


if __name__ == '__main__':
    main()
