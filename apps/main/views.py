from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from apps.common.common_data_imports import data
from apps.common.features import *
from apps.common.models import Status


@login_required
def main(request, publication_id=None):
    """
    Go to main page
    :param request:
    :param publication_id:
    :return:
    """
    data['my_profil'] = get_object_user(request.user.id)
    data["mode"] = "publications"
    data['user'] = request.user
    try:
        object_user = get_object_user(request.user.id)
    except:
        return redirect('/')
    else:
        data['class_single_publication'] = ""
        if publication_id:
            status = Status.objects.get(id=publication_id)
            data['all_status'] = [(get_object_user(status.author), status)]
            data["mode"] = "one_publication"
            data['class_single_publication'] = "class_single_publication"
        else:
            data['all_status'] = [(get_object_user(status.author), status) for status in object_user.get_status_main()]
        if object_user.get_type_user() == "Company":
            data['contacts'] = [get_object_user(contact.id) for contact in object_user.employees.all()]
        else:
            data['contacts'] = [get_object_user(contact.id) for contact in object_user.contacts.all()]
        return render(request, 'main/main.html', data)