from django.db import models
import os

def file_path(instace,filename):
    path = "documents/"
    format = 'uploaded-' + filename
    return os.path.join(path,format)

# Create your models here.

class FileHandler(models.Model):

    file_upload = models.FileField(upload_to=file_path)

    def __str__(self) -> str:
        return str(self.file_upload)