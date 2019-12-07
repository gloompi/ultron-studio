from django.contrib import admin
from .models import SkillsSection, Skill

class SkillsSectionAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')

class SkillAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')

# Register your models here.
admin.site.register(SkillsSection, SkillsSectionAdmin)
admin.site.register(Skill, SkillAdmin)