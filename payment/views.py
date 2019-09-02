from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from business.models import Sentence


@login_required
def init_pay(request):
    if request.method == 'POST':
        sentence_id = request.POST.get('sentence_id')
        suggest_price = request.POST.get('suggest_price')
        sentence = get_object_or_404(Sentence, id=sentence_id)
        return render(request, "init_pay.html", {"sentence": sentence,
                                                 "suggest_price": suggest_price})
    else:
        return render(request, "init_pay.html")
