from django.urls import path

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/ap/', views.dashboard_ap, name='dashboard_ap'),
    path('dashboard/tr/', views.dashboard_tr, name='dashboard_tr'),
    ]