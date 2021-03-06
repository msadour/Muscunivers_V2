# Generated by Django 2.0.1 on 2019-02-10 14:41

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=500)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('author', models.ForeignKey(blank=True, on_delete=True, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=500)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('author', models.ForeignKey(blank=True, on_delete=True, related_name='status_author', to=settings.AUTH_USER_MODEL)),
                ('comments', models.ManyToManyField(blank=True, default=[], to='publication.Comment')),
            ],
        ),
    ]
