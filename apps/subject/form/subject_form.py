from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class SubjectForm(forms.Form):
    name = forms.CharField(label="",
                               required=False,
                                widget=forms.Textarea(attrs={'width':"100%",
                                                             'cols' : "70",
                                                             'rows': "1",
                                                             'placeholder' : 'Theme du sujet',
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


class UpdateSubjectForm(forms.Form):
    name = forms.CharField(label="",
                           required=False,
                           widget=forms.Textarea(attrs={'width': "100%",
                                                        'cols': "70",
                                                        'rows': "1",
                                                        'id': '',
                                                        'style': 'resize:none;'}))

    description = forms.CharField(label="",
                           required=False,
                           widget=forms.Textarea(attrs={'width': "100%",
                                                        'cols': "70",
                                                        'rows': "1",
                                                        'id': '',
                                                        'style': 'resize:none;'}))

    def __init__(self, subject, *args, **kwargs):
        super(UpdateSubjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = subject.name
        self.fields['description'].widget.attrs['placeholder'] = subject.description