from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Comment(models.Model):
    message = models.TextField(max_length=500)
    date = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(User, related_name='comment_author', on_delete=True, blank=True, null=False)


class Status(models.Model):
    message = models.TextField(max_length=500)
    date = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(User, related_name='status_author', on_delete=True, blank=True, null=False)
    comments = models.ManyToManyField(Comment, blank=True, default=[])

    def get_comments(self):
        return [comment for comment in self.comments.all().order_by('-date')]
