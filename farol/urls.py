from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('status',views.statuspage, name='status_page.html'),
    ]