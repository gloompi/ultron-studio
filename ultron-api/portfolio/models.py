from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Portfolio(models.Model):
  title = models.CharField(max_length=30)
  description = models.CharField(max_length=40)

class Work(models.Model):
  coverImg = models.ImageField()
  title = models.CharField(max_length=30)
  description = HTMLField()
  link = models.CharField(max_length=50)
  portfolio = models.ForeignKey(
    'portfolio.Portfolio',
    related_name='works',
    on_delete=models.CASCADE,
  )

class Category(models.Model):
  name = models.CharField(max_length=20)
  works = models.ManyToManyField(Work, related_name='categories')

  class Meta:
    verbose_name_plural = 'Categories'

class Tech(models.Model):
  name = models.CharField(max_length=20)
  works = models.ManyToManyField(Work, related_name='technologies')

class Image(models.Model):
  src = models.ImageField(unique=True)
  work = models.ForeignKey(
    'portfolio.Work',
    related_name='images',
    on_delete=models.CASCADE,
  )
