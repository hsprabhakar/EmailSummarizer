from django.contrib import admin
from .models import UserProfile, Topic  # Import your models

# Register each model
admin.site.register(UserProfile)
admin.site.register(Topic)
