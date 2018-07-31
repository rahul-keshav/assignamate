# Generated by Django 2.0.1 on 2018-07-31 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignment', '0033_assignment_number_of_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignmentlikecounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_like', models.IntegerField(default=0)),
                ('assignment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assignment.Assignment')),
                ('like', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
