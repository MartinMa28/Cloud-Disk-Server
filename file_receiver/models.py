from django.db import models

# Create your models here.
class File(models.Model):
    file_name = models.CharField(max_length=100)
    file_data = models.FileField(upload_to='files/')

    def __str__(self):
        return self.file_name