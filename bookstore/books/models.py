from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=218)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=218)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl=models.CharField(max_length=218,null=True)
    shortDescription=models.CharField(max_length=218,null=True)
    longDescription=models.TextField(null=True)
    author = models.ManyToManyField(Author)
    image = models.ImageField(upload_to="image",null=True)

    def __str__(self):
        return f"{self.id} {self.title}"

class Review(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to="image/review",null=True)

