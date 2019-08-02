from django.contrib import admin
from business import models

# Business
admin.site.register(models.Sentence)
admin.site.register(models.Takhasos)
admin.site.register(models.SentenceStatus)
admin.site.register(models.ContentType)
admin.site.register(models.FileGallery)
admin.site.register(models.SuggestStatus)
admin.site.register(models.Suggest)
admin.site.register(models.UserType)
admin.site.register(models.UserStatus)
admin.site.register(models.Maharat)
admin.site.register(models.Dashboard)
admin.site.register(models.Report)
admin.site.register(models.Judgment)
admin.site.register(models.JudgmentsStatus)
admin.site.register(models.PaymentStatus)
