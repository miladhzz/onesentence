from django.db import models
from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError

# Create your models here.


class Takhasos(models.Model):
    title = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.title


class ContentType(models.Model):
    title = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.title


class FileGallery(models.Model):
    title = models.CharField(max_length=100, unique=True)
    file = models.FileField(upload_to='media/upload/files')

    def __str__(self):
        return self.title


class Sentence(models.Model):
    takhasos = models.ForeignKey(Takhasos, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    mohlat_rooz = models.IntegerField()
    mohlat_saat = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    word_count = models.IntegerField()
    zemanat_price = models.DecimalField(decimal_places=0, max_digits=10)
    price = models.DecimalField(decimal_places=0, max_digits=10)
    # content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    content_text = models.TextField(max_length=500)
    # content_file = models.FileField(upload_to='media/upload/sentence_files', blank=True)

    def __str__(self):
        return 'Time: %s, %s' % (self.create_time, self.takhasos.title)


class SuggestStatus(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Suggest(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    mojri = models.ForeignKey(User, on_delete=models.CASCADE)
    zaman_pishnahadi = models.IntegerField()
    mablagh_pishnahadi = models.DecimalField(decimal_places=0, max_digits=10)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, blank=True)
    status = models.ForeignKey(SuggestStatus, on_delete=models.DO_NOTHING)
    score = models.IntegerField()
    time_tahvil = models.DateTimeField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    content_text = models.TextField(blank=True)
    content_file = models.FileField(upload_to='media/upload/suggest_files', null=True)
    judgment_request = models.BooleanField()
    judgment_user_request = models.ForeignKey(User, blank=True, on_delete=models.DO_NOTHING,
                                              related_name='user_request')
    judgment_description = models.TextField(blank=True, max_length=500)


class UserType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class UserStatus(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Maharat(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Dashboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mojodi = models.DecimalField(decimal_places=0, max_digits=10)
    user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)
    user_status = models.ForeignKey(UserStatus, on_delete=models.DO_NOTHING)
    resume_description = models.TextField(max_length=500)
    resume_file = models.ForeignKey(FileGallery, on_delete=models.DO_NOTHING)
    maharat = models.ManyToManyField(Maharat, blank=True)
    rate = models.DecimalField(decimal_places=2, max_digits=3)


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)



