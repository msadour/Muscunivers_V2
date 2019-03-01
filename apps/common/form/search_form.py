from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label='',
                             max_length=100,
                             required=False,
                            widget = forms.TextInput(attrs={'placeholder': 'Recherche',
                                                            'style': 'width:450%; line-height: 2em; border-radius: 5px;',
                                                            'class': 'input_form_search',
                                                            'id': 'input_search'
                                                            })
                             )