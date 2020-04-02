from rest_framework import serializers

from .. import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'first_name', 'last_name',]


class SentenceSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = models.Sentence
        exclude = ['payment_status', 'status', 'translator', ]
        depth = 1
