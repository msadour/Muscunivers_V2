from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Message(models.Model):
    message = models.CharField(max_length=300)
    date = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(User, related_name='author_message', on_delete=True, blank=True, null=False)
    receiver = models.ForeignKey(User, related_name='receiver_receiver', on_delete=True, blank=True, null=False)
    is_read = models.BooleanField(default=False)


class Discussion(models.Model):
    messages = models.ManyToManyField(Message, blank=True, default=[])
    members = models.ManyToManyField(User, blank=True, default=[])
    date_creation = models.DateTimeField(default=datetime.now, blank=True)

    def get_contact_discussion(self, user):
        members_list = [member for member in self.members.all()]
        if user in members_list:
            members_list.remove(user)
        return members_list[0]
        # return "".join(members_list)

    def contain_messages_unread(self):
        contain_messages_unread = False
        for message in self.messages.all():
            if message.is_read == False:
                contain_messages_unread = True
        return contain_messages_unread