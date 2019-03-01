from django.contrib.auth.models import User
import pytest
import re
from datetime import datetime
from apps.publication.models import Status, Comment
from apps.common.models import Notification
from apps.profil.models import Product, Coaching, Athlete, Coach, Company
from apps.chatting.models import Message, Discussion
from apps.event.models import Event
from apps.subject.models import Subject
from django.contrib.auth import authenticate, login, logout


def check_error_user(username, mail, password, password_again):
    errors = []

    if username != '':
        check_username = User.objects.filter(username=username).count()
        if check_username > 0:
            errors.append('Nom d\'utilisateur déja existant.')

    if mail != '':
        check_mail = User.objects.filter(email=mail).count()
        if check_mail > 0:
            errors.append('Email déja existant.')

        if re.compile("[^@]+@[^@]+\.[^@]+").search(mail) is None:
            errors.append("Email invalide")

    if password != '':
        if re.compile("^[A-Za-z0-9]{6,}$").search(password) is None:
            errors.append("Le mot de passe doit contenir au moins 6 caractères")

        if password != password_again:
            errors.append('Les mots de passes doivent etre identique')

        if re.compile("^([A-Za-z1-9]{2,})$").search(username) is None:
            errors.append("Le nom d'utilisateur doit contenir au moins deux caractères.")

    return errors


@pytest.mark.django_db
def publish_message(author, message):
    status = Status(message=message, author=author, date=datetime.now())
    status.save()
    return message


def comment(request):
    author_comment = request.user
    message = request.GET.get('comment', None)
    id_status = request.GET.get('id_status', None)
    status = Status.objects.get(id=id_status)
    comment = Comment(message=message, author=author_comment, date=datetime.now())
    comment.save()
    status.comments.add(comment)

    if status.author.username != author_comment.username:
        name = author_comment.username + " a commenté votre publication."
        notification = Notification(
                                    name=name,
                                    status=status,
                                    for_who=status.author,
                                    from_who=author_comment,
                                    is_read=False)

        notification.save()


def get_object_user(id):
    if Athlete.objects.filter(user_id=id).count() > 0:
        current_user = Athlete.objects.get(user_id=id)
    elif Coach.objects.filter(user_id=id).count() > 0:
        current_user = Coach.objects.get(user_id=id)
    elif Company.objects.filter(user_id=id).count() > 0:
        current_user = Company.objects.get(user_id=id)
    else:
        current_user = None

    return current_user


def search(current_user, search, category=None):
    results_athlete = [(athlete, current_user.get_type_connection(athlete)) for athlete in Athlete.objects.filter(
                                   user_id__in=User.objects.filter(username__contains=search))]

    results_coach = [(coach, current_user.get_type_connection(coach)) for coach in Coach.objects.filter(
        user_id__in=User.objects.filter(username__contains=search))]

    results_company = [(company, current_user.get_type_connection(company)) for company in Company.objects.filter(
                                   user_id__in=User.objects.filter(username__contains=search))]

    if not category:
        return results_athlete, results_coach, results_company
    else:
        if category == "Athlete":
            return results_athlete
        elif category == "Coach":
            return results_coach
        else:
            return results_company


def connection_user(username, password):
    info_connection = {'errors': [], 'user': None}
    if User.objects.filter(username=username).count() == 0:
        info_connection['errors'].append('Username not exist..')

    try:
        username = User.objects.get(username=username).username
        if authenticate(username=username, password=password) is None:
            info_connection['errors'].append('Username or password is not valid ..')
    except:
        info_connection['errors'].append('Username or password is not valid ..')
    else:
        user = authenticate(username=username, password=password)

    if len(info_connection['errors']) == 0:
        info_connection['user'] = user

    return info_connection


def inscription_user(type_user, form):
    info_connection = {'errors': [], 'user': None}
    if type_user == "Company":
        username = form.get("name")
        date_creation = form.get("date_creation")
        category = form.get("category")
        place = form.get("city")
        email = form.get("email")
        password = form.get("password")
        password_again = form.get("password_again")
        profil_picture = form.get("profil_picture")

        info_connection['errors'] = check_error_user(username, email, password, password_again)

        if len(info_connection['errors']) == 0:
            user = User.objects.create_user(username, email, password)
            user.save()
            info_connection['user'] = user
            profil_picture.name = str(user.id)
            profil_picture.width = 370
            profil_picture.height = 348
            company = Company(user=user,
                              name=username,
                              date_creation=date_creation,
                              category=category,
                              place=place,
                              profil_picture=profil_picture)
            company.save()
    else:
        username = form.get("user_name")
        email = form.get("email")
        first_name = form.get("first_name")
        last_name = form.get("last_name")
        city = form.get("city")
        password = form.get("password")
        password_again = form.get("password_again")
        type_user = form.get("type_user")
        gender = form.get("gender")
        profil_picture = form.get("profil_picture")

        info_connection['errors'] = check_error_user(username, email, password, password_again)
        if len(info_connection['errors']) == 0:
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            user.save()
            info_connection['user'] = user
            profil_picture.name = str(user.id)
            if type_user == "Athlete":
                new_object = Athlete(user=user, gender=gender, city=city, profil_picture=profil_picture)
            else:
                new_object = Coach(user=user, gender=gender, city=city, profil_picture=profil_picture)
            new_object.save()
    return info_connection


def send_message_to_contact(my_user, user_contact, message):
    if not my_user.get_discussion_with_user(user_contact.user):
        discussion = Discussion(date_creation=datetime.now())
        discussion.save()
        discussion.members.add(my_user.user)
        discussion.members.add(user_contact.user)
        my_user.discussions.add(discussion)
        user_contact.discussions.add(discussion)
    else:
        discussion = my_user.get_discussion_with_user(user_contact.user)

    message = Message(message=message, date=datetime.now(), author=my_user.user, receiver=user_contact.user)
    message.save()
    discussion.messages.add(message)


def create_service(type_product, form, user):
    name = form.get("name")
    price = form.get("price")
    description = form.get("description")
    if type_product == "coaching":
        coaching = Coaching(name=name, price=price, description=description)
        coaching.save()
        user.coachings.add(coaching)
    else:
        weblink = form.get("weblink")
        product = Product(name=name, price=price, description=description, weblink=weblink)
        product.save()
        user.products.add(product)


def insert_event_bdd(form, user):
    name = form.get("name")
    description = form.get("description")
    date_begin = form.get("date_begin")
    date_end = form.get("date_end")
    event = Event(name=name, description=description, date_begin=date_begin, date_end=date_end, author=user)
    event.save()


def insert_subject_bdd(form, user):
    name = form.get("name")
    description = form.get("description")
    new_subject = Subject(name=name, description=description, date_creation=datetime.now(), author=user)
    # import pdb ; pdb.set_trace()
    new_subject.save()
    new_subject.followers.add(user)
    # new_subject.save()


def update_profil_data(user_profil, form):
    if user_profil.get_type_user() == 'Company':
        if form.get("name") != '':
            user_profil.name = form.get("name")
            user_profil.user.username = form.get("name")
        if form.get("date_creation") != '':
            user_profil.date_creation = form.get("date_creation")
        if form.get("category") != '':
            user_profil.category = form.get("category")
        if form.get("place") != '':
            user_profil.place = form.get("place")
        if form.get("email") != '':
            user_profil.user.email = form.get("email")
        if form.get("password") != '':
            if form.cleaned_data["password"] == form.get("password_again"):
                user_profil.user.set_password(form.get("password"))
    else:
        if form.get("user_name") != '':
            user_profil.user.username = form.get("user_name")
        if form.get("first_name") != '':
            user_profil.user.first_name = form.get("first_name")
        if form.get("last_name") != '':
            user_profil.user.last_name = form.get("last_name")
        if form.get("place") != '':
            user_profil.city = form.get("place")
        if form.get("email") != '':
            user_profil.user.email = form.get("email")
        if form.get("password") != '':
            if form.get("password") == form.get("password_again"):
                user_profil.user.set_password(form.get("password"))
    user_profil.user.save()
    user_profil.save()

