from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import json
from apps.common.common_data_imports import data
from apps.common.features import *
from .form import message_form
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string


def get_number_new_message(request):
    discussions_with_new_message = []
    for discussion in get_object_user(request.user).discussions.all():
        for message in discussion.messages.all():
            if message.is_read == False and message.author != request.user:
                if discussion not in discussions_with_new_message:
                    discussions_with_new_message.append(discussion)
    return HttpResponse(json.dumps({'num_discussion': len(discussions_with_new_message)}))


@login_required
def go_to_chat(request, contact=None):
    data['my_profil'] = get_object_user(request.user.id)
    my_user = get_object_user(request.user.id)
    if len(my_user.discussions.all()) == 0:
        if not contact:
            contact = "No contact"
        else:
            contact = get_object_user(User.objects.get(username=contact).id)

        current_conversation = []
        conversation = []

    else:
        if not contact:
            contact = get_object_user(my_user.get_last_discussion().get_contact_discussion(request.user))
        else:
            contact = get_object_user(User.objects.get(username=contact).id)

        if my_user.get_discussion_with_user(contact.user):
            current_conversation = [(get_object_user(item.author), item) for item in my_user.get_discussion_with_user(contact.user).messages.all()]
        else:
            current_conversation = []
        conversation = [(get_object_user(discussion[0].id), discussion[1]) for discussion in my_user.get_discussions()]

    if len(current_conversation) > 0:
        for message in current_conversation:
            message[1].is_read = True
            message[1].save()

    data['current_conversation'] = current_conversation
    data['conversations'] = conversation

    data['contact'] = contact
    data['user'] = request.user
    data['search_form_user'] = message_form.SearchUserMessageForm(request.POST)
    data['message_form'] = message_form.MessageForm(request.POST)
    return render(request, 'chatting/conversation.html', data)


def update_conversation(request):
    contact = get_object_user(int(request.GET.get('contact', None)))
    my_user = get_object_user(request.user.id)
    data['current_conversation'] = [(get_object_user(item.author), item) for item in
                            my_user.get_discussion_with_user(contact.user).messages.all()]
    data['user'] = request.user

    html = render_to_string('chatting/messages.html', data)

    return HttpResponse(html)


@login_required
def go_to_chat_by_search_form(request):
    if request.method == 'POST':
        search_form_chat = message_form.SearchUserMessageForm(request.POST)
        if search_form_chat.is_valid():
            search = search_form_chat.cleaned_data["search_user"]
            contact = User.objects.get(username=search)
            return HttpResponseRedirect('/chattings/' + contact.username)


def see_conversations_by_search(request):
    my_user = get_object_user(request.user)
    search = request.GET.get('search', None)
    result = []
    if my_user.get_type_user() == 'Company':
        contacts = my_user.employees.all()
    else:
        contacts = my_user.contacts.all()

    for contact in contacts:
        if search in contact.username:
            result.append(contact.username)
    return HttpResponse(json.dumps({'result': result}))


def send_message(request):
    my_user = get_object_user(request.user.id)
    user_contact = get_object_user(int(request.GET.get('user', None)))
    message = request.GET.get('message', None)

    send_message_to_contact(my_user, user_contact, message)

    return HttpResponse(json.dumps({'ok': 'ok'}))
