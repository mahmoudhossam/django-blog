from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField(blank=False)
    title = models.CharField(blank=False, max_length=100)
    created_at = models.DateField(blank=False)

