from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Tariff(models.Model):
  name = models.CharField(max_length=20)
  price = models.IntegerField()
  period = models.CharField(max_length=20)

class Feature(models.Model):
  text = HTMLField()
  tariffs = models.ManyToManyField(Tariff, related_name='features')