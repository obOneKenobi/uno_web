from django.contrib import admin

# Register your models here.
from .models import Web

class Web_admin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")

admin.site.register(Web, Web_admin)