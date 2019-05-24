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


class SuggestStatus(models.Model):
    title = models.CharField(max_length=30)


class Suggest(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    mojri = models.ForeignKey(User, on_delete=models.CASCADE)
    zaman_pishnahadi = models.IntegerField()
    mablagh_pishnahadi = models.DecimalField()
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)
    status = models.ForeignKey(SuggestStatus, on_delete=models.DO_NOTHING)
    score = models.IntegerField()
    time_tahvil = models.DateTimeField(null=True, blank=True)
    file = models.ForeignKey(FileGallery, on_delete=models.DO_NOTHING)
    file_type = models.ForeignKey(FileType, on_delete=models.DO_NOTHING)
    judgment_request = models.BooleanField()
    judgment_user_request = models.ForeignKey(User, null=True, blank=True)
    judgment_description = models.TextField(blank=True, max_length=500)


class UserType(models.Model):
    title = models.CharField(max_length=100)


class UserStatus(models.Model):
    title = models.CharField(max_length=100)


class Maharat(models.Model):
    title = models.CharField(max_length=100)


class Dashboard(models.Model):
    mojodi = models.DecimalField()
    user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)
    user_status = models.ForeignKey(UserStatus, on_delete=models.DO_NOTHING)
    resume_description = models.TextField(max_length=500)
    resume_file = models.ForeignKey(FileGallery, on_delete=models.DO_NOTHING)
    maharat = models.ManyToManyField(Maharat, blank=True)
    rate = models.DecimalField()


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE())
    create_time = models.DateTimeField(auto_now_add=True)



