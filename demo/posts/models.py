from django.db import models

# Create your models here.
class posts(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  slug = models.SlugField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  banner = models.ImageField(default="fallback.png", blank=True)
  
  def __str__(self):
    return self.title