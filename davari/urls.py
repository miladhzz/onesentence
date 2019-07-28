from django.urls import path

from davari import views


app_name = 'davari'

urlpatterns = [
    path('dashboard/da/', views.dashboard_da, name='dashboard_da'),
    path('dashboard/da/<int:suggest_id>', views.sentence_detail_davari,
         name="sentence_detail_davari"),

    ]
