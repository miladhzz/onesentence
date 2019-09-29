from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from business.models import Sentence, Suggest, Dashboard
from onesentence.enums import PaymentEnum
from .forms import PaymentForm
from django.shortcuts import redirect
from decimal import Decimal
from zeep import Client
from django.http import HttpResponse


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
            mojodi_applicant = Dashboard.objects.get(user=sentence.user).mojodi
            mojodi_translator = Dashboard.objects.get(user=sentence.translator).mojodi
            # todo log transactions
            Dashboard.objects.filter(user=sentence.user).update(mojodi=mojodi_applicant - Decimal(mablagh))
            Dashboard.objects.filter(user=sentence.translator).update(mojodi=mojodi_translator + Decimal(mablagh))
            Sentence.objects.filter(id=sentence_id).update(payment_status=PaymentEnum.payed.value)
            return redirect('dashboard:sentence_detail_dashboard', sentence_id=sentence.id,
                            sentence_title=sentence.title)
    else:
        form = PaymentForm()

    return render(request, "init_pay.html", {"sentence": sentence,
                                             "suggest": suggest,
                                             "form": form})


MERCHANT = ''
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000  # Toman / Required
description = "تست جنگو"  # Required
email = 'miladhzz@gmail.com'  # Optional
mobile = '09384677005'  # Optional
CallbackURL = 'http://127.0.0.1:8000/verify/'  # Important: need to edit for really server.


@login_required
def charge(request):
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


@login_required
def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')

