

from django.contrib import admin
from django.urls import path, include
from max import views

app_name = 'max'

urlpatterns = [
path('', views.index, name='index')
    ]