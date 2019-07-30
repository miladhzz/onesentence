from django import forms
from business import models


class UpdateJudgmentForm(forms.ModelForm):
    class Meta:
        model = models.Judgment
        fields = ('judgment_won_user',)