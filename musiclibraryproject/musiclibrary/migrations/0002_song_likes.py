# Generated by Django 3.1.8 on 2021-07-08 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclibrary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
