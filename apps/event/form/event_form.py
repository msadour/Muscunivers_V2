from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class EventForm(forms.Form):
    name = forms.CharField(label="",
                               required=False,
                                widget=forms.Textarea(attrs={'width':"100%",
                                                             'cols' : "70",
                                                             'rows': "1",
                                                             'placeholder' : 'Nom du groupe',
                                                             'id': '',
                                                             'style':'resize:none;'}))

    description = forms.CharField(label="",
                               required=False,
                                widget=forms.Textarea(attrs={'width':"100%",
                                                             'cols' : "70",
                                                             'rows': "1",
                                                             'placeholder' : 'Description',
                                                             'id': '',
                                                             'style':'resize:none;'}))

    date_begin = forms.DateField(widget=forms.SelectDateWidget(attrs={}))

    date_end = forms.DateField(widget=forms.SelectDateWidget(attrs={}))