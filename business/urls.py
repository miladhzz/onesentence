from django.urls import path

from business import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_sentence/', views.add_sentence, name='add_sentence'),
    path('submit_suggest/', views.submit_suggest, name='submit_suggest'),
    path('sentence_list/', views.SentenceList.as_view(), name='sentence_list')
    ]
