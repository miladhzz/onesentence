from django.shortcuts import render


def init_pay(request):
    if request.method == 'POST':
        sentence = 'test sentence'
        return render(request, "init_pay.html", {"sentence": sentence})
    else:
        return render(request, "init_pay.html")