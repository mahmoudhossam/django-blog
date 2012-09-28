from django.db import models

class Post(models.Model):
    title = models.CharField(blank=False, max_length=100)
    text = models.TextField(blank=False)
    created_at = models.DateField(blank=False, auto_now_add=True)
