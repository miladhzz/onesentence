from django.db import models
from business.models import Suggest
from django.contrib.auth.models import User


class Judgment(models.Model):
    suggest = models.ForeignKey(Suggest, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=500)
    barandeh = models.ForeignKey(User, on_delete=models.CASCADE)
