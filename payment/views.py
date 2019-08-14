from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def init_pay(request):
    if request.method == 'POST':
        sentence_id = request.POST.get('sentence_id')
        suggest_price = request.POST.get('suggest_price')
        sentence = 'test sentence'
        return render(request, "init_pay.html", {"sentence": sentence})
    else:
        return render(request, "init_pay.html")
