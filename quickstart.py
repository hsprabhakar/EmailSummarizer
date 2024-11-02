import base64
import quopri
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import json

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
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=2).execute()
    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')
    else:
        # Loop through the messages and print their details
        i = 1
        for message in messages:
            print(f'Message {i}: \n')
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            headers = msg['payload']['headers']
            fHeaders = filterHeaders(headers)
            body, body_size = getBody(msg)
            if body_size > 8000: # Max character count for ChatGPT is 16000 but we will stick with half of that for now
                print(f'Skipping email from "{fHeaders[0]}" due to size of body: {body_size} bytes\n')
                i = i+1
                continue        

            data = convertToJson(fHeaders, body)
            print(data)
            print()
            i = i+1
            # print("From: ", fHeaders[0])
            # print("Subject: ", fHeaders[1])
            # print("Date: ", fHeaders[2])
            # print("Body: ", body if body else "No body found.")
            # print()

def convertToJson(headers, body):
    x = {
        "From": headers[0],
        "Subject": headers[1],
        "Date": headers[2],
        "Body": body
    }
    return json.dumps(x)
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

def getBody(msg):
    """
    Extracts and returns the body of an email message.

    Args:
        msg (dict): A dictionary representing an email message, where the 'payload' key contains
                    the 'body' and 'headers' keys.

    Returns:
        str: The body of the email message, if it exists. Otherwise, returns None.
    """
    body = None
    if 'parts' in msg['payload']:
        for part in msg['payload']['parts']:
            if part['mimeType'] == 'text/plain':
                body = part['body'].get('data')
                break
            elif part['mimeType'] == 'text/html':
                body = part['body'].get('data')
                body = cleanHTML(body)
                break
    else:
        body = msg['payload']['body'].get('data')
        if msg['payload']['mimeType'] == 'text/html':
            body = cleanHTML(body)

    if body:
        body = base64.urlsafe_b64decode(body).decode('utf-8')
        
    body_size = len(body.encode('utf-8')) if body else 0 # len counts number of characters
        
    return body, body_size

def cleanHTML(html_content):
    """
    Cleans and returns the HTML content of an email message.

    Args:
        html (str): The HTML content of an email message.

    Returns:
        str: The cleaned HTML content of the email message.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    for content in soup(['style', 'script']):
        content.decompose()
    return soup.get_text(separator='\n', strip=True)



if __name__ == '__main__':
    main()
