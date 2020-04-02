from django.urls import path
from business import views
from django.contrib.auth import views as auth_views

from .api.router import router
from .api.views import SentenceList


app_name = 'business'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_sentence/', views.add_sentence, name='add_sentence'),
    # path('submit_suggest/', views.submit_suggest, name='submit_suggest'),
    path('sentence_list/', views.SentenceList.as_view(), name='sentence_list'),
    path('sentence/<int:sentence_id>/<str:sentence_title>', views.sentence_detail, name='sentence_detail'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),

    path('api/v1/sentence-list/', SentenceList.as_view(), name='sentence_list_api'),
    ]

# urlpatterns += router.urls

