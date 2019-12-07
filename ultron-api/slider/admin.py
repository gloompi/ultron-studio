from django.contrib import admin
from .models import Slide

class SlideAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description')

# Register your models here.
admin.site.register(Slide, SlideAdmin)