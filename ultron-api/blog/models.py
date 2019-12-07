from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=50)
  content = HTMLField()
  background_image = models.ImageField(unique=True)

  class Meta:
    verbose_name = "Article"
    verbose_name_plural = "Articles"