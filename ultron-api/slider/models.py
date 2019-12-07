from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Slide(models.Model):
  title = models.CharField(max_length=50)
  subtitle = models.CharField(max_length=50, blank=True)
  description = HTMLField(blank=True)
  background_image = models.ImageField(blank=False, unique=True)

  class Meta:
    verbose_name = "Slide"
    verbose_name_plural = "Slides"