from django.shortcuts import render
from .models import Subject
from .form import subject_form
from apps.common.common_data_imports import data


def go_to_subject(request, id_subject, window='main'):
    current_subject = Subject.objects.get(id=id_subject)
    data['current_subject'] = current_subject
    data['current_user'] = request.user
    data['window'] = window

    data['mode'] = 'my_profil'
    if window == 'main':
        data['all_status'] = current_subject.status.all()
    if window == 'followers':
        data['followers'] = current_subject.members.all()
    if window == 'manage':
        data['update_subject_form'] = subject_form.UpdateSubjectForm(current_subject)
    return render(request, 'subject/base.html', data)


def add_members(request):
    pass


def delete_members(request):
    pass
