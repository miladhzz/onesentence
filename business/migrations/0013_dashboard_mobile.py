# Generated by Django 2.1.1 on 2019-10-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0012_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='mobile',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
