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
        instance.word_count = len(instance.content_text)
        instance.save()
        return instance


class SubmitSuggestForm(forms.ModelForm):
    class Meta:
        model = models.Suggest
        fields = ('mablagh_pishnahadi', 'description', 'content_type', 'content_text', 'content_file',
                   'content_text')

    def save(self, request):
        instance = super(SubmitSuggestForm, self).save(commit=False)
        instance.mojri = request.user
        instance.status = models.SuggestStatus.objects.get(id=1)
        instance.sentence = instance.sentence
        instance.save()
        return instance
