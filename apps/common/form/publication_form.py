from django import forms
from django.utils.safestring import mark_safe


class StatusForm(forms.Form):
    message = forms.CharField(label="",
                               required=False,
                                widget=forms.Textarea(attrs={'width':"100%",
                                                             'border': 'none',
                                                             'cols' : "70",
                                                             'rows': "5",
                                                             'placeholder' : 'Quoi de neuf?',
                                                             'id': 'message_publication_form',
                                                             'style':'resize:none;'}))


class StatusToWallUserForm(forms.Form):
    message = forms.CharField(label="",
                               required=False,
                                widget=forms.Textarea(attrs={'width':"100%",
                                                             'border': 'none',
                                                             'cols' : "70",
                                                             'rows': "5",
                                                             'placeholder' : 'Dites lui quelque chose ...',
                                                             'id': 'message_publication_form',
                                                             'style':'resize:none;'}))


class CommentForm(forms.Form):
    comment = forms.CharField(label="",
                               required=False,
                                widget=forms.Textarea(attrs={'width':"100%",
                                                             'style': 'line-height: 2em;',
                                                             'cols' : "40",
                                                             'rows': "1",
                                                             'class': 'comment_input',
                                                             'name': 'comment',
                                                             #'id': 'comment_publication_form',
                                                             'placeholder' : 'Un commentaire ?',
                                                             'style':'resize:none;'}))