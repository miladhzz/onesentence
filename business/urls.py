from django.urls import path

from business import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_sentence/', views.add_sentence, name='add_sentence')
    ]
