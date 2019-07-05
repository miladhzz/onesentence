from django.urls import path

from business import views

app_name = 'business'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_sentence/', views.add_sentence, name='add_sentence'),
    # path('submit_suggest/', views.submit_suggest, name='submit_suggest'),
    path('sentence_list/', views.SentenceList.as_view(), name='sentence_list'),
    path('sentence/<int:sentence_id>/<str:sentence_title>', views.sentence_detail, name='sentence_detail'),
    ]
