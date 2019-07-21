from django.urls import path

from davari import views

app_name = 'davari'

urlpatterns = [
    path('dashboard/da/', views.dashboard_da, name='dashboard_da'),
    ]
