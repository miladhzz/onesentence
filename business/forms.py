from django import forms
from business import models


# from django.core import validators


class AddSentenceForm(forms.ModelForm):
    class Meta:
        model = models.Sentence
        fields = ('takhasos', 'mohlat_rooz', 'mohlat_saat', 'zemanat_price', 'price',
                   'content_text')

    def save(self, request):
        instance = super(AddSentenceForm, self).save(commit=False)
        instance.user = request.user
        instance.status = models.Status.objects.get(id=1)
        instance.word_count = 0
        instance.save()
        return instance
