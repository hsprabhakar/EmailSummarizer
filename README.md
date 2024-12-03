# EmailSummarizer

## How to run demo

Create a Virtual env.

Windows: ```python -m venv myenv```
Mac OS: ```python3 -m venv myenv```

then activate

Windows: ```myenv\Scripts\activate```
Mac OS: ```source myenv/bin/activate```

then install dependencies

```pip install -r requirements.txt```

then create your OAuth2 credentials 

* Go to APIs & Services > Credentials.
* Click Create Credentials and choose OAuth 2.0 Client IDs.
* Configure the consent screen if not done already.
* Set up OAuth for a Web Application or Desktop App depending on your use case.
* Add the redirect URIs: ```http://localhost:8000/oauth2callback/```.
* Download the credentials file (a credentials.json) and keep it in your root directory of this project

Run using ```python .\quickstart.py```



## How to run the main app

Ensure you have your credentials setup on google cloud.
Make sure your credentials have the following scopes:
* openid
* userinfo.email
* userinfo.profile
* gmail.readonly

These scopes are defined as well inside views.py. These are essential to allow the app to read Gmail and read details using the openid api. 


### Run Backend:
Navigate into EmailSummarizer folder and run ```python manage.py runserver```

Head to http://localhost:8000/

### Run Frontend:
In a second terminal, navigate into frontend folder and run ```npm run dev```

Head to http://localhost:3000/
