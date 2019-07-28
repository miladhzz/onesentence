from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from business.models import Judgment


@login_required
def dashboard_da(request):
    judgments = Judgment.objects.all()
    return render(request, "davar_dashboard.html", {'judgments': judgments})


@login_required
def sentence_detail_davari(request, suggest_id):
    judgment = get_object_or_404(Judgment, suggest_id=suggest_id)
    return render(request, "sentence_detail_davari.html", {'judgment': judgment})
