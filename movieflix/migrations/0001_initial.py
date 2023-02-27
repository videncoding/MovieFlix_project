# Generated by Django 3.2.18 on 2023-02-27 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('Movie_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=50)),
                ('Poster', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=200)),
                ('IMDB_Rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('User_ID', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('Role', models.CharField(blank=True, max_length=20)),
                ('Genres', models.CharField(blank=True, max_length=20)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WatchedList',
            fields=[
                ('WatchedList_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Movie_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.movie')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('Rating_ID', models.AutoField(primary_key=True, serialize=False)),
                ('User_Rating', models.IntegerField(default=0)),
                ('Movie_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.movie')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('Comment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Comment', models.CharField(max_length=200)),
                ('Movie_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.movie')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.userprofile')),
            ],
        ),
    ]
