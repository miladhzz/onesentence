from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from business.models import Sentence, Suggest
from .forms import PaymentForm
from django.shortcuts import redirect


@login_required
def init_pay(request):
    sentence = {}
    suggest = {}
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            return redirect('business:home')
    else:
        form = PaymentForm()
        sentence_id = request.GET.get("sentence")
        suggest_id = request.GET.get("suggest")
        sentence = get_object_or_404(Sentence, id=sentence_id)
        suggest = get_object_or_404(Suggest, id=suggest_id, sentence_id=sentence_id)

    return render(request, "init_pay.html", {"sentence": sentence,
                                             "suggest": suggest,
                                             "form": form})
