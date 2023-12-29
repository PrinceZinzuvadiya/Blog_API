from django.db import models

# Create your models here.
class blogs (models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=500)
    updated=models.DateTimeField(auto_now=True)