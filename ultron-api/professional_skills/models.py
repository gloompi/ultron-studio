from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class SkillsSection(models.Model):
  title = models.CharField(max_length=30)
  description = HTMLField()

class Skill(models.Model):
  icon = models.CharField(max_length=20)
  title = models.CharField(max_length=30)
  description = HTMLField()
  knowledge_percent = models.IntegerField()
  skills_section = models.ForeignKey(
    'professional_skills.SkillsSection',
    related_name='skills',
    on_delete=models.CASCADE,
  )