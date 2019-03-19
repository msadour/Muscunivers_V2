from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.common.form import search_form, update_profil_form
from apps.common.common_data_imports import data
from apps.common.features import *
from apps.common.models import RequestContact


def go_to_main(request):
    """
    Go to main page
    :param request:
    :return:
    """
    data['my_profil'] = get_object_user(request.user.id)
    return redirect('/main')


def go_to_settings(request):
    """
    Go to settings page
    :param request:
    :return:
    """
    data['my_profil'] = get_object_user(request.user.id)
    data['informations'] = get_object_user(request.user.id)
    if data['my_profil'].get_type_user() == 'Company':
        data['update_form'] = update_profil_form.UpdateProfilCompanyForm(data['my_profil'])
    else:
        data['update_form'] = update_profil_form.UpdateProfilForm(data['my_profil'])
    return render(request, 'common/settings.html', data)


def go_to_request_contact(request):
    """
    Go to request page
    :param request:
    :return:
    """
    data['my_profil'] = get_object_user(request.user.id)
    data['user'] = request.user
    data['requests_contact'] = [get_object_user(contact.from_request.id) for contact in RequestContact.objects.filter(to_request=request.user)]
    return render(request, 'common/request_contact.html', data)


@login_required
def search_users(request):
    """
    Go to result of user searching
    :param request:
    :return:
    """
    data['my_profil'] = get_object_user(request.user.id)
    form = search_form.SearchForm(request.POST)
    if form.is_valid():
        search_user = form.cleaned_data["search"]
        data['search'] = search_user
        data["athlete_url"] = "Athlete"
        data["coach_url"] = "Coach"
        data["company_url"] = "Company"
        data["all_url"] = "All"
        current_user = get_object_user(request.user)
        data["results_athlete"], data["results_coach"], data["results_company"] = search(current_user, search_user)
        data["current_user"] = current_user
    return render(request, 'common/search/result_search_all.html', data)


@login_required
def go_to_notifications(request):
    """
    Go to notification page
    :param request:
    :return:
    """
    data['my_profil'] = get_object_user(request.user.id)
    data['notifications'] = Notification.objects.filter(for_who=request.user).order_by('-date')
    return render(request, 'common/notifications.html', data)
