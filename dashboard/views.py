from django.shortcuts import render

# Create your views here.


def dashboard_ap(request):
    return render(request, 'applicant_dashboard.html')


def dashboard_tr(request):
    return render(request, 'translator_dashboard.html')