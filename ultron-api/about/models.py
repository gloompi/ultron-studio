from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class About(models.Model):
  title = models.CharField(max_length=50)
  description = HTMLField()

  class Meta:
    verbose_name = "About"
    verbose_name_plural = "About"

class Item(models.Model):
  icon = models.CharField(max_length=15)
  title = models.CharField(max_length=30)
  description = HTMLField()
  about = models.ForeignKey(
    'about.About',
    related_name='items',
    on_delete=models.CASCADE,
  )