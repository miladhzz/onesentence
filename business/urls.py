from django.urls import path

from business import views

urlpatterns = [
    path('', views.home, name='home'),
    ]
