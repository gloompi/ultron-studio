from django.contrib import admin
from .models import About, Item

class AboutAdmin(admin.ModelAdmin):
  list_display = ('title', )

class ItemAdmin(admin.ModelAdmin):
  list_display = ('title', )

# Register your models here.
admin.site.register(About, AboutAdmin)
admin.site.register(Item, ItemAdmin)