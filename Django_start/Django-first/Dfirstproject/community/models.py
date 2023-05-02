from django.db import models

# Create your models here.

class Posting(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    category = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content = models.TextField('Content')

    def __str__(self):
        return self.title