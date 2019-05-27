from django import forms
from business import models


class AddSentenceForm(forms.ModelForm):
    class Meta:
        model = models.Sentence
        fields = ('takhasos','mohlat_rooz', 'mohlat_saat', 'zemanat_price', 'price',
                  'content_type', 'content_text', 'content_file')

    def save(self, request):
        instance = super(AddSentenceForm, self).save(commit=False)
        instance.user = request.user
        instance.save()
        return instance
