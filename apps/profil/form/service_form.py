from django import forms
from django.utils.safestring import mark_safe

attrs_form = {
    'width':"100%",
    'border': 'none',
    'cols' : "22",
    'rows': "1",
    'placeholder' : 'http://website.com',
    'style':'resize:none;'

}

class ProductForm(forms.Form):
    name = forms.CharField(label=mark_safe('Nom du produit '), max_length=100, required=False)
    price = forms.CharField(label=mark_safe('Prix '), max_length=100, required=False)
    description = forms.CharField(label=mark_safe('Description '), max_length=100, required=False)
    weblink = forms.CharField(label=mark_safe('Lien web '), max_length=100, required=False,
                              widget=forms.Textarea(attrs={'width':"100%",
                                                             'border': 'none',
                                                             'cols' : "22",
                                                             'rows': "1",
                                                             'placeholder' : 'http://lesite.com',
                                                             'style':'resize:none;'}))


class CoachingForm(forms.Form):
    name = forms.CharField(label=mark_safe('Nom du coaching '), max_length=100, required=False)
    price = forms.CharField(label=mark_safe('Prix '), max_length=100, required=False)
    description = forms.CharField(label=mark_safe('Description '), max_length=100, required=False)




    # name = models.CharField(max_length=100, default="")
    # price = models.IntegerField(default=0)
    # description = models.CharField(max_length=100, default="This user doesn't put description")
    # suscriber = models.ForeignKey(User, related_name='coaching_coach', on_delete=True, blank=True, null=True)