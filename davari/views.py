from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from business.models import Judgment, Dashboard
from davari.forms import UpdateJudgmentForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from decimal import Decimal


@login_required
def dashboard_da(request):
    judgments = Judgment.objects.all()
    return render(request, "davar_dashboard.html", {'judgments': judgments})


@login_required
def sentence_detail_davari(request, suggest_id):
    judgment = get_object_or_404(Judgment, suggest_id=suggest_id)
    sentence = judgment.suggest.sentence
    if request.method == "POST":
        judgment_form = UpdateJudgmentForm(request.POST, instance=judgment)
        mablagh = request.POST.get('mablagh')
        if judgment_form.is_valid():
            judgment_form = judgment_form.save(commit=False)
            judgment_form.save()
            # todo log transactions
            mojodi_applicant = Dashboard.objects.get(user=sentence.user).mojodi
            mojodi_translator = Dashboard.objects.get(user=sentence.translator).mojodi
            Dashboard.objects.filter(user=sentence.user).update(mojodi=mojodi_applicant - Decimal(mablagh))
            Dashboard.objects.filter(user=sentence.translator).update(mojodi=mojodi_translator + Decimal(mablagh))
            return redirect("business:home")
    else:
        judgment_form = UpdateJudgmentForm(instance=judgment)
    return render(request, "sentence_detail_davari.html", {'judgment': judgment,
                                                           'judgment_form': judgment_form})
