from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  slug = models.SlugField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  banner = models.ImageField(default="fallback.png", blank=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

  def __str__(self):
    return self.title