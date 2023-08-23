from django.contrib import admin
from .models import Aplicação

# Register your models here.
admin.site.site_header = 'Status Page - Command Center'

@admin.register(Aplicação)
class AplicaçãoAdmin(admin.ModelAdmin):
    list_display = ('nome','status')
    list_filter = ('status',)