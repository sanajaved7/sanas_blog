from django.db import models
from django.utils import timezone


class Tag(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def unpublish(self):
        self.published_date = None
        self.save()
