from django import forms
from business import models
from onesentence.enums import SuggestEnum, SentenceEnum


# from django.core import validators


class AddSentenceForm(forms.ModelForm):
    class Meta:
        model = models.Sentence
        fields = ('title', 'takhasos', 'mohlat_rooz', 'mohlat_saat', 'zemanat_price', 'price',
                  'content_text')

    def save(self, request):
        instance = super(AddSentenceForm, self).save(commit=False)
        instance.user = request.user
        # default sentence status 2 (sabt nahaei)
        instance.status = models.SentenceStatus.objects.get(id=SentenceEnum.Saved.value)
        instance.word_count = len(instance.content_text)
        instance.save()
        return instance

    def clean_zemanat_price(self, *args, **kwargs):
        mojodi = models.Dashboard.objects.get(user=self.user).mojodi
        zemanat_price = self.cleaned_data.get("zemanat_price")
        if zemanat_price <= mojodi:
            return zemanat_price
        else:
            raise forms.ValidationError("مبلغ ضمانت از موجودی شما بیشتر است.")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AddSentenceForm, self).__init__(*args, **kwargs)


class SubmitSuggestForm(forms.ModelForm):
    class Meta:
        model = models.Suggest
        fields = ('mablagh_pishnahadi', 'description')
        # widgets = {'name': forms.HiddenInput()}

    def clean_mablagh_pishnahadi(self, *args, **kwargs):
        mojodi = models.Dashboard.objects.get(user=self.user).mojodi
        mablagh_pishnahadi = self.cleaned_data.get("mablagh_pishnahadi")

        if mojodi < self.sentence.zemanat_price:
            raise forms.ValidationError("مبلغ ضمانت از موجودی شما بیشتر است.")
        if mablagh_pishnahadi <= mojodi:
            return mablagh_pishnahadi
        else:
            raise forms.ValidationError("مبلغ پیشنهادی از موجودی شما بیشتر است.")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.sentence = kwargs.pop('sentence', None)
        super(SubmitSuggestForm, self).__init__(*args, **kwargs)
