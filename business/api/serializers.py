from rest_framework import serializers

from .. import models


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sentence
        exclude = ['payment_status', 'status', 'translator', ]
        depth = 1
