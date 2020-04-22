from django.db import models

# Create your models here.
class File(models.Model):
    file_name = models.CharField(max_length=100)
    file_data = models.FileField(upload_to='files/')

    def delete(self, *args, **kwargs):
        self.file_data.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.file_name