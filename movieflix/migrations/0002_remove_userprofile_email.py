# Generated by Django 3.2.18 on 2023-03-11 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieflix', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='Email',
        ),
    ]
