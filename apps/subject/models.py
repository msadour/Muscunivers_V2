from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from apps.publication.models import Status


class Subject(models.Model):
    name = models.TextField(max_length=500)
    description = models.TextField(max_length=500)
    date_creation = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(User, related_name='subject_author', on_delete=True, blank=True, null=False)
    followers = models.ManyToManyField(User, related_name='subject_follower', blank=True, default=[])
    status = models.ManyToManyField(Status, related_name='%(class)s_status', blank=True, default=[])