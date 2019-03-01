from datetime import datetime
from apps.chatting.models import Discussion
from apps.common.models import RequestContact
from apps.subject.models import Subject
from apps.event.models import Event
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q

from apps.common.models import Status


def upload_location(instance_user_id):
    return "profil_pictures/" + instance_user_id + ".png"


class Product(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
    description = models.CharField( max_length=100, default="")
    weblink = models.CharField(max_length=100, default="")


class Coaching(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100, default="This user doesn't put description")


class Profil(models.Model):
    user = models.ForeignKey(User, related_name='%(class)s_user', on_delete=True, blank=True, null=True, default=None)
    contacts = models.ManyToManyField(User, related_name='%(class)s_contact', blank=True, default=[])
    status = models.ManyToManyField(Status, related_name='%(class)s_status', blank=True, default=[])
    discussions = models.ManyToManyField(Discussion, related_name='%(class)s_discussion', blank=True, default=[])
    profil_picture = models.ImageField(null=True, blank=True)

    def get_type_user(self):
        return self.__class__.__name__

    def get_discussions(self):
        discussions = []
        for discussion in self.discussions.all():
            discussions.append([(member, discussion.contain_messages_unread()) for member in discussion.members.all().exclude(username=self.user.username)][0])
        return discussions

    def get_last_discussion(self):
        return self.discussions.all().order_by('-date_creation')[0]

    def get_discussion_with_user(self, user):
        return [discussion for discussion in self.discussions.all() if user in discussion.members.all()][0]

    def get_status_main(self):
        return Status.objects.filter(Q(author_id__in = [contact.id for contact in self.contacts.all()]) | Q(author_id = self.user.id)).order_by('-date')

    def get_my_status(self):
        return Status.objects.filter(author_id = self.user.id).order_by('-date')

    def get_publications(self):
        return [publication for publication in self.publications]

    def get_my_event(self):
        return [event for event in Event.objects.all() if self.user in event.members.all()]

    def get_my_subjects(self):
        return [subject for subject in Subject.objects.all() if self.user in subject.followers.all()]

    def get_type_connection(self, user_profil):
        if self.user == user_profil.user:
            return "me"
        elif user_profil.user in self.contacts.all():
            return "connected"
        elif RequestContact.objects.filter(from_request=user_profil.user, to_request=self.user).count():
            return "wait_answer"
        elif RequestContact.objects.filter(from_request=self.user, to_request=user_profil.user).count():
            return "request_sent"
        else:
            if user_profil.get_type_user() == "Company":
                return "join"
            else:
                return "add_contact"

    class Meta:
        abstract = True


class Athlete(Profil):
    gender = models.CharField(max_length=5, default='', blank=True, null=True)
    city = models.CharField(max_length=300, default='')


class Coach(Profil):
    gender = models.CharField(max_length=5, default='', blank=True, null=True)
    coachings = models.ManyToManyField(Coaching, related_name='coaching_coach', blank=True, default=[])
    city = models.CharField(max_length=300, default='')


class Company(Profil):
    name = models.CharField(max_length=300)
    date_creation = models.DateTimeField(default=datetime.now, blank=True, null=False)  # '%Y-%m-%d %H:%M:%S'
    category = models.CharField(max_length=300)
    place = models.CharField(max_length=300, default='')
    employees = models.ManyToManyField(User, related_name='employee_company', blank=True, default=[])
    products = models.ManyToManyField(Product, related_name='products_company', blank=True, default=[])