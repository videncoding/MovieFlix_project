# Generated by Django 2.1.5 on 2023-03-05 18:43

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
            name='Comment',
            fields=[
                ('Comment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('Movie_ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(max_length=50)),
                ('Poster', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=200)),
                ('IMDB_Rating', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('Rating_ID', models.AutoField(primary_key=True, serialize=False)),
                ('User_Rating', models.IntegerField(default=0)),
                ('Movie_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.CharField(blank=True, max_length=20)),
                ('Genres', models.CharField(blank=True, max_length=20)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WatchedList',
            fields=[
                ('WatchedList_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Movie_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.Movie')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Movie_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.Movie'),
        ),
        migrations.AddField(
            model_name='comment',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.UserProfile'),
        ),
    ]
