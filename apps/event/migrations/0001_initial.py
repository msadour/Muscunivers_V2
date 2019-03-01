# Generated by Django 2.0.1 on 2019-02-10 14:41

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publication', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=500)),
                ('description', models.TextField(max_length=500)),
                ('date_creation', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('date_begin', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('date_end', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('author', models.ForeignKey(blank=True, on_delete=True, related_name='event_author', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, default=[], related_name='event_members', to=settings.AUTH_USER_MODEL)),
                ('status', models.ManyToManyField(blank=True, default=[], related_name='event_status', to='publication.Status')),
            ],
        ),
    ]