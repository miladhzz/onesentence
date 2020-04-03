from rest_framework import generics
from rest_framework.permissions import AllowAny

from .. import models
from . import serializers


class SentenceList(generics.ListAPIView):
    queryset = models.Sentence.objects.all()
    serializer_class = serializers.SentenceSerializer
    # permission_classes = [AllowAny]


class SentenceDetail(generics.RetrieveAPIView):
    # lookup_field = 'word_count'
    queryset = models.Sentence.objects.all()
    serializer_class = serializers.SentenceSerializer


class AddSentence(generics.CreateAPIView):
    serializer_class = serializers.AddSentenceSerializer
