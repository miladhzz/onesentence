from django.db import models
from django.contrib.auth.models import User


class TransactionType(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
