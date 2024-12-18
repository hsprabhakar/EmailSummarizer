"""
URL configuration for EmailSummarizer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('login/', views.oauth2_login, name='oauth2_login'), # Initiates OAuth flow
    path('oauth2callback/', views.oauth2_callback, name='oauth2_callback'),  # Handles redirect
    path('', views.home, name='home'),  # New home view for the root URL
    path('api/auth/google', views.oauth2_login, name='oauth2_login'),  # New view for Google sign-in
    path('api/summarize/top_emails', views.top_emails, name='top_emails'),  # API endpoint for summarize emails button
]
