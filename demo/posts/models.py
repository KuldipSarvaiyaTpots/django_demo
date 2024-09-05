from django.db import models

# Create your models here.
class posts(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  slug = models.SlugField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)