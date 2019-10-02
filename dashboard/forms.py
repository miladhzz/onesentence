from django import forms
from business import models


class EditCompleteFileForm(forms.ModelForm):
    class Meta:
        model = models.Suggest
        fields = ('completeFile',)


class SubmitJudgmentForm(forms.ModelForm):
    class Meta:
        model = models.Judgment
        fields = ('judgment_description',)


class ChargeForm(forms.Form):
    mablagh = forms.IntegerField(label='مبلغ (تومان)', min_value=1000, max_value=1000000)

    def clean_mablagh(self):
        mablagh = self.cleaned_data['mablagh']
        if mablagh < 1000 or mablagh > 1000000:
            raise forms.ValidationError('مبلغ وارد شده معتبر نیست.')
