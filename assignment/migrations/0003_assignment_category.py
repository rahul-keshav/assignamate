# Generated by Django 2.0 on 2018-09-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20180815_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='category',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]