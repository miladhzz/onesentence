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