from django.contrib import admin
from .models import  acortador_url

@admin.register(acortador_url)
class acortador_urlAdmin(admin.ModelAdmin):
    list_display = ('acor_url', 'id',)
