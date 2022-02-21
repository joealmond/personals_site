# Generated by Django 4.0.2 on 2022-02-21 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('excerpt', models.CharField(max_length=500)),
                ('image_name', models.CharField(max_length=80)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(default='')),
                ('content', models.TextField()),
            ],
        ),
    ]
