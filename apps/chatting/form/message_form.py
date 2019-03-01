from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class MessageForm(forms.Form):
    message = forms.CharField(label="",
                               required=False,
                                widget=forms.Textarea(attrs={'width':"100%",
                                                             'cols' : "70",
                                                             'rows': "1",
                                                             'placeholder' : 'Ecrivez votre message..',
                                                             'id': 'message_form',
                                                             'style':'resize:none;'}))


class SearchUserMessageForm(forms.Form):
    search_user = forms.CharField(label="",
                               required=False,
                                widget=forms.Textarea(attrs={'width':"90%",
                                                             'cols' : "30",
                                                             'rows': "1",
                                                             'id': 'input_search_user_chatting',
                                                             'placeholder' : 'Recherchez un contact',
                                                             'style':'resize:none;'}))