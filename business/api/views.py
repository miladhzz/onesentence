from rest_framework import generics
from rest_framework.permissions import AllowAny

from .. import models
from . import serializers


class SentenceList(generics.ListAPIView):
    queryset = models.Sentence.objects.all()
    serializer_class = serializers.SentenceSerializer
    permission_classes = [AllowAny]
