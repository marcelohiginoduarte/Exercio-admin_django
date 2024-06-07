from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Define uma URL para a visão 'index'
]