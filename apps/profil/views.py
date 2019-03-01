from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import json
from apps.common.common_data_imports import data
from apps.common.features import *
from .form import update_profil_form, service_form
from apps.event.form import event_form
from apps.subject.form import subject_form
from .models import Product, Coaching
from django.http import HttpResponse


@login_required
def go_to_profil(request, id_user=None, window=None):
    data['my_profil'] = get_object_user(request.user.id)
    if id_user:
        user_profil = get_object_user(User.objects.get(id=id_user))
    else:
        user_profil = get_object_user(User.objects.get(id=request.user.id))

    if not window:
        window = "wall"

    data['mode'] = "my_profil" if id_user == request.user.id or not id_user else "profil_contact"
    data['type_contact'] = get_object_user(request.user.id).get_type_connection(user_profil)
    data['window'] = window
    data['user'] = request.user
    data['window'] = window
    data["current_user"] = user_profil
    if window == 'wall':
        data['all_status'] = [(user_profil, status) for status in user_profil.get_my_status()]

    elif window == 'subjects':
        data['subject_form'] = subject_form.SubjectForm(request.POST)
        data['subject_profil'] = [one_subject for one_subject in user_profil.get_my_subjects()]
    elif window == 'events':
        data['event_form'] = event_form.EventForm(request.POST)
        data['events_profil'] = [one_event for one_event in user_profil.get_my_events()]

    elif window == 'contacts':
        data[window] = [get_object_user(contact.id) for contact in user_profil.contacts.all()]
    elif window == 'employees':
        data[window] = [get_object_user(employee.id) for employee in user_profil.employees.all()]
    elif window == 'products':
        data['product_form'] = service_form.ProductForm(request.POST)
        data[window] = user_profil.products.all()
    elif window == 'coachings':
        data['coaching_form'] = service_form.CoachingForm(request.POST)
        data[window] = user_profil.coachings.all()

    return render(request, 'profil/profil.html', data)


def create_product(request):
    if request.method == "POST":
        form = service_form.ProductForm(request.POST)
        if form.is_valid():
            create_service("product", form.cleaned_data, get_object_user(request.user))

    return go_to_profil(request, window='products')


def delete_product(request):
    current_company = get_object_user(request.user.id)
    id_product = request.GET.get('id_product', None)
    # import pdb ; pdb.set_trace()
    product = Product.objects.get(id=id_product)
    current_company.products.remove(product)
    product.delete()
    return HttpResponse(json.dumps({'ok': 'ok'}))


# ------------------------------------------ Coaching ------------------------------------------


def create_coaching(request):
    if request.method == "POST":
        form = service_form.CoachingForm(request.POST)
        if form.is_valid():
            create_service("coaching", form.cleaned_data, get_object_user(request.user))

    return go_to_profil(request, window='coachings')


def delete_coaching(request):
    current_coach = get_object_user(request.user.id)
    id_coaching = request.GET.get('id_coaching', None)
    coaching = Coaching.objects.get(id=id_coaching)
    current_coach.coachings.remove(coaching)
    coaching.delete()
    return HttpResponse(json.dumps({'ok': 'ok'}))


# ------------------------------------------ Event ------------------------------------------

def create_event(request):
    if request.method == "POST":
        form = event_form.EventForm(request.POST)
        if form.is_valid():
            insert_event_bdd(form.cleaned_data, request.user)

    return go_to_profil(request, window='events')


# ------------------------------------------ Event ------------------------------------------

def create_subject(request):
    if request.method == "POST":
        form = subject_form.SubjectForm(request.POST)
        if form.is_valid():
            # import pdb; pdb.set_trace()
            insert_subject_bdd(form.cleaned_data, request.user)

    return go_to_profil(request, window='subjects')

















