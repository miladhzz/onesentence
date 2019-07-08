from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from business.models import Suggest, Sentence
# Create your views here.


def dashboard_ap(request):
    my_sentence = Sentence.objects.filter(user=request.user)
    return render(request, 'applicant_dashboard.html', {'my_sentence': my_sentence})


@login_required
def dashboard_tr(request):
    my_suggests = Suggest.objects.filter(mojri=request.user)
    return render(request, 'translator_dashboard.html', {'my_suggests': my_suggests})