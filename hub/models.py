from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.

class Post(models.Model):
    tags = TaggableManager()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Video(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/default.jpg')

    def add(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class FastNews(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def add(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(default=1)
    location = models.CharField(max_length=200, default="Header")

    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def addItem(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
