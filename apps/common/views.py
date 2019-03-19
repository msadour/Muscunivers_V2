from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json
from apps.common.form import search_form, update_profil_form
from apps.common.common_data_imports import data
from apps.common.features import *
from django.http import HttpResponse
from apps.menu.views import go_to_settings
from .models import RequestContact
from django.db.models import Q


# ------------------- request contact -------------------


def accept_or_decline(request):
    """
    Accept or decline an invitation from an user
    :param request:
    :param contact:
    :return:
    """
    user_id = request.GET.get('id_user', None)
    type_contact = request.GET.get('type_contact', None)
    user_contact = User.objects.get(id=user_id)
    if type_contact == "accept":
        contact = get_object_user(user_contact.id)
        me = get_object_user(request.user.id)
        if contact.get_type_user() == "Company":
            contact.employees.add(me.user)
        elif me.get_type_user() == "Company":
            me.employees.add(contact.user)
        else:
            me.contacts.add(contact.user)
            contact.contacts.add(me.user)

    request_contact = RequestContact.objects.get(Q(from_request=user_contact) & Q(to_request=request.user))
    request_contact.delete()
    return HttpResponse(json.dumps({'ok': 'ok'}))


def manage_contact(request):
    user_id = request.GET.get('id_user', None)
    type_contact = request.GET.get('type_contact', None)
    user_contact = User.objects.get(id=user_id)
    if type_contact == "add_contact" or type_contact == "add_employees":
        new_contact = RequestContact(from_request=request.user, to_request=user_contact)
        new_contact.save()
    elif type_contact == "cancel_request":
        contact = RequestContact.objects.get(Q(from_request=request.user) & Q(to_request=user_contact))
        contact.delete()
    return HttpResponse(json.dumps({'ok': 'ok'}))


def remove_contact(request):
    """
    Remove a contact
    :param request:
    :param contact:
    :return:
    """
    user_id = request.GET.get('id_user', None)
    me = get_object_user(request.user.id)
    contact_user = get_object_user(user_id)

    if me.get_type_user() == "Company":
        me.employees.remove(contact_user.user)
    # elif contact_user.get_type_user() == "Company":
    #     contact_user.employees.remove(me.user)
    else:
        me.contacts.remove(contact_user.user)
        contact_user.contacts.remove(me.user)

    return HttpResponse(json.dumps({'ok': 'ok'}))


# ------------------- search -------------------


def get_users_list_search(request):
    user_search = request.GET.get('user_search', None)
    list_users = [user.username for user in User.objects.filter(username__contains=user_search)] #string__contains=

    return HttpResponse(json.dumps({'list_users' : list_users}))


@login_required
def search_specific(request, category, what):
    """
    Search user by specification
    :param request:
    :param contact:
    :return:
    """
    data['my_profil'] = get_object_user(request.user.id)
    data['search'] = what
    data["athlete_url"] = "Athlete"
    data["coach_url"] = "Coach"
    data["company_url"] = "Company"
    data["all_url"] = "All"
    data["category"] = category
    current_user = get_object_user(request.user)
    data["current_user"] = current_user
    if not category:
        data["results_athlete"], data["results_coach"], data["results_company"] = search(current_user, what)
        return render(request, 'search/result_search_all.html', data)
    else:
        data["results"] = search(current_user, what, category)
    return render(request, 'common/search/result_search_specific.html', data)


# ------------------- Notification -------------------


def get_number_new_request_contact(request):
    """
    Get the number of new request contact
    :param request:
    :param contact:
    :return:
    """
    nb_request_contact = RequestContact.objects.filter(to_request=request.user).count()
    return HttpResponse(json.dumps({'nb_request_contact': nb_request_contact}))


def get_number_new_message(request):
    """
    Get the number of new message
    :param request:
    :param contact:
    :return:
    """
    discussions_with_new_message = []
    for discussion in get_object_user(request.user).discussions.all():
        for message in discussion.messages.all():
            if message.is_read == False and message.author != request.user:
                if discussion not in discussions_with_new_message:
                    discussions_with_new_message.append(discussion)
    return HttpResponse(json.dumps({'num_discussion': len(discussions_with_new_message)}))


def update_new_notifications(request):
    """
    Going to chatroom
    :param request:
    :param contact:
    :return:
    """
    Notification.objects.filter(for_who=request.user, is_read=False).update(is_read=True)
    return HttpResponse(json.dumps({'ok': 'ok'}))


def get_number_new_notifications(request):
    """

    :param request:
    :param contact:
    :return:
    """
    nb_notifications = Notification.objects.filter(for_who=request.user, is_read=False).count()
    return HttpResponse(json.dumps({'nb_notifications': nb_notifications}))


# ------------------- settings -------------------


def update_profil(request):
    user_profil = get_object_user(request.user)
    if request.method == "POST":
        if user_profil.get_type_user() == 'Company':
            form = update_profil_form.UpdateProfilCompanyForm(user_profil, request.POST, request.FILES)
        else:
            form = update_profil_form.UpdateProfilForm(user_profil, request.POST, request.FILES)
        if form.is_valid():
            try:
                update_profil_data(user_profil, form.cleaned_data)
            except:
                pass

        return go_to_settings(request)