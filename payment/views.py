from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from business.models import Sentence, Suggest, Dashboard, Payment
from onesentence.enums import PaymentEnum
from .forms import PaymentForm
from django.shortcuts import redirect
from decimal import Decimal
from zeep import Client
from django.http import HttpResponse
from onesentence.settings import MERCHANT, CallbackURL
from dashboard.forms import ChargeForm


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


client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')


@login_required
def charge(request):
    if request.method == 'POST':
        form = ChargeForm(request.POST)
        if form.is_valid():
            dashboard_instance = get_object_or_404(Dashboard, user=request.user)
            description = "شارژ حساب کاربری"  # Required
            email = dashboard_instance.user.email
            mobile = dashboard_instance.mobile
            amount = request.POST.get('mablagh')
            result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
            if result.Status == 100 and len(result.Authority) == 36:
                payment = Payment(amount=amount, authority=int(result.Authority), dashboard=dashboard_instance)
                payment.save()
                return redirect('https://www.zarinpal.com/pg/StartPay/' + str(int(result.Authority)))
            else:
                return HttpResponse('Error code: ' + str(result.Status))
    else:
        form = ChargeForm()
    return render(request, "charge.html", {"form": form})


@login_required
def callback(request):
    if request.GET.get('Status') == 'OK':
        authority = int(request.GET['Authority'])
        payment = get_object_or_404(Payment, authority=authority)
        result = client.service.PaymentVerification(MERCHANT, authority, payment.amount)
        if result.Status == 100:
            payment.status = result.Status  # 100 complete
            payment.ref_id = result.RefID
            payment.save()

            dashboard_instance = payment.dashboard
            dashboard_instance.mojodi += payment.amount
            dashboard_instance.save()

            return render(request, 'callback.html', {'refId': payment.ref_id})
        elif result.Status == 101:
            payment = get_object_or_404(Payment, authority=authority)
            return render(request, 'callback.html', {'refId': payment.refId})
        else:
            return HttpResponse('تراکنش ناموفق.\nStatus: ' + str(result.Status) +
                                '<a href="http://onesentence.ir">بازگشت</a>')
    else:
        return HttpResponse('پرداخت توسط کاربر لغو شد' + '<a href="http://onesentence.ir">بازگشت</a>')

