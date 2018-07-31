# Generated by Django 2.0.1 on 2018-07-31 00:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignment', '0031_assignment_answered_by_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment_answered_by',
            name='like',
        ),
        migrations.AddField(
            model_name='assignment',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='is_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
