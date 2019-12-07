from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')

# Register your models here.
admin.site.register(Contact, ContactAdmin)