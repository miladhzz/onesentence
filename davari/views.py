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
    user_applicant = sentence.user
    user_translator = sentence.translator
    if request.method == "POST":
        judgment_form = UpdateJudgmentForm(request.POST, instance=judgment)
        mablagh = request.POST.get('mablagh')
        if judgment_form.is_valid():
            judgment_form = judgment_form.save(commit=False)
            judgment_form.save()

            if user_applicant == judgment.judgment_won_user:
                user_loser = user_translator
            else:
                user_loser = user_applicant

            # todo log transactions
            mojodi_won_user = Dashboard.objects.get(user=judgment.judgment_won_user).mojodi
            mojodi_lose_user = Dashboard.objects.get(user=user_loser).mojodi

            Dashboard.objects.filter(user=judgment.judgment_won_user).update(mojodi=mojodi_won_user + Decimal(mablagh))
            Dashboard.objects.filter(user=user_loser).update(mojodi=mojodi_lose_user - Decimal(mablagh))
            return redirect("business:home")
    else:
        judgment_form = UpdateJudgmentForm(instance=judgment)
    return render(request, "sentence_detail_davari.html", {'judgment': judgment,
                                                           'judgment_form': judgment_form})
