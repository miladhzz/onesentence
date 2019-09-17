from django import forms
from business import models
from onesentence.enums import SuggestEnum, SentenceEnum
from business.models import Dashboard

# from django.core import validators


class PaymentForm(forms.Form):
        mablagh = forms.IntegerField(label='مبلغ قابل پرداخت')
        accept = forms.BooleanField(label='مبلغ مورد تایید است',)
        sentence_id = forms.IntegerField()
        suggest_id = forms.IntegerField()

        def clean_mablagh(self, *args, **kwargs):
            mablagh = self.cleaned_data.get("mablagh")
            mojodi = models.Dashboard.objects.get(user=self.user).mojodi
            if mablagh > mojodi:
                raise forms.ValidationError("مبلغ از موجودی شما بیشتر است.")

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(PaymentForm, self).__init__(*args, **kwargs)

        # def save(self):
        #     instance = super(PaymentForm, self).save(commit=False)
        #     instance.save()
        #
        #     return instance
