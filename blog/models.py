from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)

    def get_absolute_url(self):
        return reverse('detail', args=[self.slug])
