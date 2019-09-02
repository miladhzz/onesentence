from django import forms
from business import models
from onesentence.enums import SuggestEnum, SentenceEnum


# from django.core import validators


class PaymentForm(forms.Form):
        mablagh = forms.IntegerField(label='مبلغ قابل پرداخت')
        accept = forms.BooleanField(label='مبلغ مورد تایید است',)

        def clean_mablagh(self, *args, **kwargs):
            mablagh = self.cleaned_data.get("mablagh")
            if mablagh == 5000:
                raise forms.ValidationError("مبلغ ضمانت از موجودی شما بیشتر است.")
    # def save(self, request):
    #     instance = super(PaymentForm, self).save(commit=False)
    #     instance.user = request.user
    #     # default sentence status 2 (sabt nahaei)
    #     instance.status = models.SentenceStatus.objects.get(id=SentenceEnum.Saved.value)
    #     instance.word_count = len(instance.content_text)
    #     instance.save()
    #     return instance
    #
    # def clean_zemanat_price(self, *args, **kwargs):
    #     mojodi = models.Dashboard.objects.get(user=self.user).mojodi
    #     zemanat_price = self.cleaned_data.get("zemanat_price")
    #     if zemanat_price <= mojodi:
    #         return zemanat_price
    #     else:
    #         raise forms.ValidationError("مبلغ ضمانت از موجودی شما بیشتر است.")
    #
    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #     super(PaymentForm, self).__init__(*args, **kwargs)