# Generated by Django 2.0.1 on 2018-06-05 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0016_blogsite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='blog_image/')),
                ('blog_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Blogsite')),
            ],
        ),
    ]
