from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=256)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
