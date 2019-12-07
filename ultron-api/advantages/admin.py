from django.contrib import admin
from .models import AdvantagesSection, Advantage

class AdvantagesSectionAdmin(admin.ModelAdmin):
  list_display = ('title', )

class AdvantageAdmin(admin.ModelAdmin):
  list_display = ('title', )

# Register your models here.
admin.site.register(AdvantagesSection, AdvantagesSectionAdmin)
admin.site.register(Advantage, AdvantageAdmin)
