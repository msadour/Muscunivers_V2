from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from apps.publication.models import Status


class RequestContact(models.Model):
    from_request = models.ForeignKey(User, related_name='from_request', on_delete=True, blank=True, null=False)
    to_request = models.ForeignKey(User, related_name='to_request', on_delete=True, blank=True, null=False)


class Notification(models.Model):
    name = models.CharField(max_length=300)
    status = models.ForeignKey(Status, related_name="status_notification", on_delete=True, blank=True, null=True)
    for_who = models.ForeignKey(User, related_name="for_who", on_delete=True, blank=True, null=True)
    from_who = models.ForeignKey(User, related_name="from_who", on_delete=True, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True, null=False)
    is_read = models.BooleanField(default=False)