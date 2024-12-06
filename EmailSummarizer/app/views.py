#from django.shortcuts import render
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from google.auth.transport import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .models import UserProfile
from django.contrib.auth.models import User
from .LLM import llm_summarize_JSON
from .utils.helpers import clean_llm_response
import os
import base64

# Create your views here.
# Set your SCOPES and redirect URI
SCOPES = ['openid', 'https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
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
    print(authorization_url)
    print(state)
    request.session['state'] = state  # Store the state in the session
    return JsonResponse({"redirect_url": authorization_url})

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

    # Save the credentials
    credentials = flow.credentials
    request.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
    request_adapter = requests.Request()
    user_info = id_token.verify_oauth2_token(credentials.id_token, request_adapter)
    # Extract email and name
    email = user_info.get('email')
    name = user_info.get('name')
    request.session['email'] = email
    request.session['name'] = name
    
    request.session['email'] = user_info.get('email')
    request.session['name'] = user_info.get('name')

    try:
        user = User.objects.get(email=email);
        print(f"User {user.username} exists, skipping creation.")
    except User.DoesNotExist:

        user=User(username = user_info.get('name'), email = user_info.get('email'))
        user.save()

    user_profile, created = UserProfile.objects.get_or_create(
        user=user,
        defaults={
            'access_token': credentials.token,
            'refresh_token': credentials.refresh_token,
        }
    )
    if not created:
        user_profile.access_token = credentials.token
        user_profile.refresh_token = credentials.refresh_token
        user_profile.save()

    try:
        user_info = id_token.verify_oauth2_token(credentials.id_token, request_adapter)
    except ValueError as e:
        return JsonResponse({"error": "Invalid token"}, status=400)
    print({"message": f"Successfully Authenticated with user info: {user_info}"})
    #TODO : change when deployed
    return HttpResponseRedirect("http://localhost:3000/home")

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
    
def top_emails(request):
    if 'credentials' not in request.session:
        return JsonResponse({"messages": "User not authenticated."})
    
    try:
        number = int(request.GET.get('number', 10))
    except ValueError:
        return JsonResponse({"error": "Invalid number parameter."}, status=400)
    
    creds = Credentials(**request.session['credentials'])
    service = build('gmail', 'v1', credentials=creds)
    try:
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=number).execute()
        messages = results.get('messages', [])

        if not messages:
            return JsonResponse({"messages": 'No messages found.'})

        email_data = []

        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            headers = {header['name']: header['value'] for header in msg['payload']['headers']}
            subject = headers.get('Subject', 'No Subject')
            sender = headers.get('From', 'Unknown Sender')
            date = headers.get('Date', 'Unknown Date')
            body = ''
            if 'parts' in msg['payload']:
                for part in msg['payload']['parts']:
                    if part['mimeType'] == 'text/plain' and 'data' in part['body']:
                        body += base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
            email_data.append({
                    "id": message['id'],
                    "sender": sender,
                    "subject": subject,
                    "date": date,
                    # "snippet": msg.get('snippet', 'No Snippet'),
                    "body": body.strip() if body else 'No Body Content'
            })
        #TODO : ensure format of email_data is correct for LLM
        raw_response = llm_summarize_JSON(json.dumps(email_data))
        llm_response = clean_llm_response(raw_response)
        print(json.dumps(email_data))
        return JsonResponse({
            "messages": email_data,
            "llm_response": llm_response
            }, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(['GET'])
def google_sign_in(request):
    return Response({"message": "Hello from Django!"})