from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Contact(models.Model):
  icon = models.CharField(max_length=25)
  title = models.CharField(max_length=25)
  description = HTMLField()

  class Meta:
    verbose_name = 'Contact'
    verbose_name_plural = 'Contacts'