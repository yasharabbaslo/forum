from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.html import mark_safe
from markdown import markdown


class Board(models.Model):

    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):

    subject = models.CharField(max_length=255)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

    def get_last_five_posts(self):
        return self.posts.order_by('-created_at')[:5]


class Post(models.Model):

    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete='cascade')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete='cascade')
    updated_by = models.ForeignKey(User, related_name='+', on_delete='cascade')

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))