from email.mime import image
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models import Model
from ckeditor.fields import RichTextField

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=80)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=80)
    excerpt = models.CharField(max_length=250)
    image_name = models.CharField(max_length=80)
    created_date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, default="", null=False)
    content = RichTextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
