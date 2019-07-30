from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from business.models import Judgment
from davari.forms import UpdateJudgmentForm
from django.shortcuts import redirect
from django.contrib.auth.models import User


@login_required
def dashboard_da(request):
    judgments = Judgment.objects.all()
    return render(request, "davar_dashboard.html", {'judgments': judgments})


@login_required
def sentence_detail_davari(request, suggest_id):
    judgment = get_object_or_404(Judgment, suggest_id=suggest_id)
    if request.method == "POST":
        user_won_id = request.POST.get('judgment_won_user')
        user_won = User.objects.get(id=user_won_id)
        judgment_form = UpdateJudgmentForm(request.POST, instance=judgment)
        if judgment_form.is_valid():
            judgment_form = judgment_form.save(commit=False)
            judgment_form.judgment_won_user = user_won
            judgment_form.save()
            return redirect("business:home")
    else:
        judgment_form = UpdateJudgmentForm(instance=judgment)
    return render(request, "sentence_detail_davari.html", {'judgment': judgment,
                                                           'judgment_form': judgment_form})
