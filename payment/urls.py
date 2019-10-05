from django.urls import path

from payment import views


app_name = 'payment'

urlpatterns = [
    path('payment/', views.init_pay, name='init_pay'),
    path('callback/', views.callback, name='callback'),
    path('charge/', views.charge, name='charge')
    ]
