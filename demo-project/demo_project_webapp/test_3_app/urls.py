from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='test-3-app-home')
]