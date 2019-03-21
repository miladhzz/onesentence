from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog import views

urlpatterns = [
    path('', views.Blog_list.as_view(), name='home'),
    path('blog/<str:slug>/', views.Blog_detail.as_view(), name='detail'),
    ]