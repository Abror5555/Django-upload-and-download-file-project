# Generated by Django 4.1.5 on 2023-01-28 06:37

from django.db import migrations, models
import download.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileHandler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_upload', models.FileField(upload_to=download.models.file_path)),
            ],
        ),
    ]