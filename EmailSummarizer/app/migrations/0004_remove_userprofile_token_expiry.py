# Generated by Django 4.2.16 on 2024-12-04 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_userprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='token_expiry',
        ),
    ]
