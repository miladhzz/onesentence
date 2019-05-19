from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Takhasos(models.Model):
    title = models.CharField(unique=True)


class Status(models.Model):
    title = models.CharField(unique=True)


class FileType(models.Model):
    title = models.CharField(unique=True)


class FileGallery(models.Model):
    title = models.CharField(max_length=100, unique=True)
    file = models.FileField(upload_to='media/upload/files')


class Sentence(models.Model):
    takhaoso = models.ForeignKey(Takhasos, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    mohlat_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    word_count = models.IntegerField()
    zemanat_price = models.DecimalField()
    price = models.DecimalField()
    content = models.TextField()
    file_type = models.ForeignKey(FileType, on_delete=models.DO_NOTHING)
    file = models.ForeignKey(FileGallery, on_delete=models.DO_NOTHING)

