from django.db import models

# Create your models here.
class Apidata(models.Model):
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=300)
    urltoimage=models.URLField()
    url=models.URLField()
    