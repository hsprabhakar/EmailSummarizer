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
        # Loop through the messages and print their details
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            headers = msg['payload']['headers']
            fHeaders = filterHeaders(headers)
            print(fHeaders)

def filterHeaders(headers):
    """
    Extracts and returns specific email headers: 'From', 'Subject', and 'Date'.

    Args:
        headers (list of dict): A list of dictionaries representing email headers, 
                                where each dictionary contains 'name' and 'value' keys.

    Returns:
        list: A list containing the 'From', 'Subject', and 'Date' values, respectively,
              extracted from the headers. If any of these headers are not present, 
              their corresponding value in the returned list will be None.
    """
    filteredHeaders = []
    sender = subject = date = None
    for header in headers:
        if header['name'] == 'From':
            sender = header['value']   
        if header['name'] == 'Subject':
            subject = header['value']
        if header['name'] == 'Date':
            date = header['value']
    filteredHeaders.append(sender)
    filteredHeaders.append(subject)
    filteredHeaders.append(date)
    return filteredHeaders

if __name__ == '__main__':
    main()
