from django.contrib import admin
from .models import Portfolio, Work, Category, Tech, Image

class PortfolioAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')

class WorkAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

class TechAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

class ImageAdmin(admin.ModelAdmin):
  list_display = ('id', 'src')

# Register your models here.
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tech, TechAdmin)
admin.site.register(Image, ImageAdmin)