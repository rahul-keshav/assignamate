# Generated by Django 2.0.1 on 2018-07-31 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0034_assignmentlikecounter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignmentlikecounter',
            old_name='like',
            new_name='user',
        ),
    ]
