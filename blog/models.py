from email.mime import image
from django.db import models
from django.utils import timezone

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
    excerpt = models.CharField(max_length=500)
    image_name = models.CharField(max_length=80)
    created_date = models.DateField(default=timezone.now)
    slug = models.SlugField(default="", null=False, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
