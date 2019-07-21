from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_da(request):
    return render(request, "davar_dashboard.html")
