#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from django.conf import settings
import os
# Create your views here.
# Set your SCOPES and redirect URI
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
REDIRECT_URI = f'{settings.LOCALHOST_URL}/oauth2callback/'

CLIENT_SECRETS_FILE = os.path.join(settings.BASE_DIR, 'credentials.json')

def home(request):
    return HttpResponse("Welcome to the Email Summarizer!")

def oauth2_login(request):
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    request.session['state'] = state  # Store the state in the session
    return HttpResponseRedirect(authorization_url)

def oauth2_callback(request):
    state = request.GET.get('state')
    if not state:
        return HttpResponse("Error: state parameter mismatch.", status=400)

    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        state=state,
        redirect_uri=REDIRECT_URI
    )

    flow.fetch_token(authorization_response=request.build_absolute_uri())

    #save the credentials
    credentials = flow.credentials
    request.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

    return HttpResponse("Authentication successful! You can now close this tab.")

def fetch_gmail_messages(request):
    if 'credentials' not in request.session:
        return HttpResponseRedirect('auth/') # return HttpResponse("User not authenticated.")
    
    creds = Credentials(**request.session['credentials'])
    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
    messages = results.get('messages', [])

    if not messages:
        return HttpResponse('No messages found.')
    else:
        output = 'Messages:<br>'
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            output += f"Snippet: {msg['snippet']}<br>"
        return HttpResponse(output)