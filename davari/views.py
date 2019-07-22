from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from business.models import Judgment


@login_required
def dashboard_da(request):
    judgments = Judgment.objects.all()
    return render(request, "davar_dashboard.html", {'judgments': judgments})
