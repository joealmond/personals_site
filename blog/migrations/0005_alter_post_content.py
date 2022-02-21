# Generated by Django 4.0.2 on 2022-02-21 11:37

import ckeditor.fields
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_author_alter_post_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
