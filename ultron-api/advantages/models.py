from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class AdvantagesSection(models.Model):
  title = models.CharField(max_length=30)
  description = HTMLField()

  class Meta:
    verbose_name = 'Advatages Section'
    verbose_name_plural = 'Advatages Section'

class Advantage(models.Model):
  icon = models.CharField(max_length=25)
  title = models.CharField(max_length=30)
  description = HTMLField()
  section = models.ForeignKey(
    'advantages.AdvantagesSection',
    related_name='advantages',
    on_delete=models.CASCADE,
  )
