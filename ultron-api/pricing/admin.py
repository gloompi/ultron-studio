from django.contrib import admin
from .models import Tariff, Feature

class TarrifAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'price')

class FeatureAdmin(admin.ModelAdmin):
  list_display = ('id', 'text')

# Register your models here.
admin.site.register(Tariff, TarrifAdmin)
admin.site.register(Feature, FeatureAdmin)