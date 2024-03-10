from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthdate = models.DateField()
    fullname = models.CharField(max_length=200)


def save(self, *args, **kwargs):
    self.fullname = f'{self.name} {self.surname}'
    super().save(*args, **kwargs)


def __str__(self):
    return self.fullname


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    release_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)


def __str__(self):
    return self.title


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    change_date = models.DateField(auto_now=True)
