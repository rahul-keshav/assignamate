# Generated by Django 2.0.1 on 2018-06-15 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0018_assignment_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment_answered_by',
            name='submitted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]