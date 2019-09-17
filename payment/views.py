from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from business.models import Sentence, Suggest, Dashboard
from onesentence.enums import PaymentEnum
from .forms import PaymentForm
from django.shortcuts import redirect
from decimal import Decimal


@login_required
def init_pay(request):
    sentence_id = request.GET.get("sentence")
    suggest_id = request.GET.get("suggest")
    sentence = get_object_or_404(Sentence, id=sentence_id)
    suggest = get_object_or_404(Suggest, id=suggest_id, sentence_id=sentence_id)

    if request.method == 'POST':
        form = PaymentForm(request.POST, user=request.user)
        if form.is_valid():
            mablagh = request.POST.get('mablagh')
            mojodi = Dashboard.objects.get(user=request.user).mojodi
            Dashboard.objects.filter(user=request.user).update(mojodi=mojodi-Decimal(mablagh))
            Sentence.objects.filter(id=sentence_id).update(payment_status=PaymentEnum.payed.value)
            return redirect('business:home')
    else:
        form = PaymentForm()

    return render(request, "init_pay.html", {"sentence": sentence,
                                             "suggest": suggest,
                                             "form": form})
