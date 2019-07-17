from django.urls import path

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/ap/', views.dashboard_ap, name='dashboard_ap'),
    path('dashboard/tr/', views.dashboard_tr, name='dashboard_tr'),
    path('dashboard/check-suggest/<int:sentence_id>', views.check_suggest, name="check_suggest"),
    path('dashboard/<int:sentence_id>/<str:sentence_title>', views.sentence_detail_dashboard,
         name="sentence_detail_dashboard")
    ]