from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class UpdateProfilForm(forms.Form):
    user_name = forms.CharField(label=mark_safe('Nom d\'utilisateur '), max_length=100, required=False)
    first_name = forms.CharField(label=mark_safe('Prénom '), max_length=100, required=False)
    last_name = forms.CharField(label=mark_safe('Nom '), max_length=100, required=False)
    place = forms.CharField(label=mark_safe('Ville '), max_length=100, required=False)
    email = forms.CharField(label=mark_safe('Email '), max_length=100, required=False)
    password = forms.CharField(label=mark_safe('Mot de passe '), max_length=100, required=False, widget=forms.PasswordInput)
    password_again = forms.CharField(label=mark_safe('Retapez votre mot de passe '), max_length=100, required=False,
                               widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        super(UpdateProfilForm, self).__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs['placeholder'] = user.user.username
        self.fields['first_name'].widget.attrs['placeholder'] = user.user.first_name
        self.fields['last_name'].widget.attrs['placeholder'] = user.user.last_name
        self.fields['place'].widget.attrs['placeholder'] = user.city
        self.fields['email'].widget.attrs['placeholder'] = user.user.email
        self.fields['password'].widget.attrs['placeholder'] = '******'
        self.fields['password_again'].widget.attrs['placeholder'] = '******'


class UpdateProfilCompanyForm(forms.Form):
    name = forms.CharField(label=mark_safe('Nom de l\'entreprise '), max_length=100, required=False)
    date_creation = forms.CharField(label=mark_safe('Date de création '), max_length=100, required=False)
    category = forms.CharField(label=mark_safe('Categorie '), max_length=100, required=False)
    place = forms.CharField(label=mark_safe('City '), max_length=100, required=False)
    email = forms.CharField(label=mark_safe('Email '), max_length=100, required=False)
    password = forms.CharField(label=mark_safe('Mot de passe '), max_length=100, required=False, widget=forms.PasswordInput)
    password_again = forms.CharField(label=mark_safe('Retapez votre mot de passe '), max_length=100, required=False,
                                     widget=forms.PasswordInput)

    def __init__(self, company, *args, **kwargs):
        super(UpdateProfilCompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = company.user.username
        self.fields['date_creation'].widget.attrs['placeholder'] = company.date_creation
        self.fields['category'].widget.attrs['placeholder'] = company.category
        self.fields['place'].widget.attrs['placeholder'] = company.place
        self.fields['email'].widget.attrs['placeholder'] = company.user.email
        self.fields['password'].widget.attrs['placeholder'] = '******'
        self.fields['password_again'].widget.attrs['placeholder'] = '******'
