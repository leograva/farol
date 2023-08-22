from django.contrib import admin
from .models import Aplicação

# Register your models here.
admin.site.site_header = 'Status Page - Command Center'
admin.site.register(Aplicação)