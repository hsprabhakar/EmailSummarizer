# EmailSummarizer

## How to run demo

Create a Virtual env on Windows.

```python -m venv myenv```
then activate

```myenv\Scripts\activate```

then install dependencies

```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```

then create your OAuth2 credentials 

* Go to APIs & Services > Credentials.
* Click Create Credentials and choose OAuth 2.0 Client IDs.
* Configure the consent screen if not done already.
* Set up OAuth for a Web Application or Desktop App depending on your use case.
* Add the redirect URIs (if needed for web apps).
* Download the credentials file (a credentials.json) and keep it in your root directory of this project

Run using ```python .\quickstart.py```