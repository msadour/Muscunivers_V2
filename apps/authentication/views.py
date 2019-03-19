from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.common.common_data_imports import data
from apps.common.features import *
from .form import authentication_form
from apps.main.views import main


def authentication(request, errors=[]):
    """
    Going to authentication page if the user isn't connected
    :param request:
    :param errors:
    :return:
    """
    redirect('/')
    if request.user.is_authenticated:
        return main(request)
    else:
        data['user'] = request.user
        data['connection_form'] = authentication_form.ConnexionForm()
        data['signup_person_form'] = authentication_form.UserForm()
        data['signup_company_form'] = authentication_form.CompanyForm()
        data['errors'] = errors
        return render(request, 'authentication/authentication.html', data)


def connection(request):
    """
    Connect a user
    :param request:
    :return:
    """
    if request.method == "POST":
        form = authentication_form.ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            info_connection = connection_user(username, password)
            if len(info_connection['errors']) == 0:
                login(request, info_connection['user'])
                return redirect('/main')
            else:
                return authentication(request, info_connection['errors'])
    else:
        form = authentication_form.ConnexionForm()

    redirect('/main')
    return main(request)


def inscription(request):
    """
    Suscription of an user
    :param request:
    :return:
    """
    if request.method == "POST":
        if 'category' in request.POST:
            form = authentication_form.CompanyForm(request.POST, request.FILES)
            type_user = 'Company'
        else:
            form = authentication_form.UserForm(request.POST, request.FILES)
            type_user = 'Person'

        if form.is_valid():
            info_inscription = inscription_user(type_user, form.cleaned_data)

            if len(info_inscription['errors']) == 0:
                login(request, info_inscription['user'])
                data['my_profil'] = get_object_user(request.user.id)
                return redirect('/main')
            else:
                return authentication(request, info_inscription['errors'])


@login_required
def log_out(request):
    """
    Logout an user
    :param request:
    :return:
    """
    data['header'] = False
    logout(request)
    return redirect('/')