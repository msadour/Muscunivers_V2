from django import forms
from django.utils.safestring import mark_safe


class ConnexionForm(forms.Form):
    username = forms.CharField(label="",
                               max_length=30,
                               required=False,
                               widget=forms.TextInput(attrs={'placeholder': '',
                                                          'style': 'width:20%;line-height: 2em;border-radius: 5px',
                                                          'class': 'form_connection',
                                                          'id': 'form_email'
                                                          })
                               )

    password = forms.CharField(label="", widget=forms.PasswordInput, required=False)

    def __init__(self, *args, **kwargs):
        super(ConnexionForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
        self.fields['password'].widget.attrs['placeholder'] = 'Mot de passe'
        self.fields['password'].widget.attrs['style'] = 'width:20%;line-height: 2em;border-radius: 5px'
        self.fields['password'].widget.attrs['class'] = 'form_connection'
        self.fields['password'].widget.attrs['id'] = 'form_password'


class UserForm(forms.Form):
    user_name = forms.CharField(label="",
                               max_length=30,
                               required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur',
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          })
                               )
    first_name = forms.CharField(label="",
                               max_length=30,
                               required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Prénom',
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          })
                               )
    last_name = forms.CharField(label="",
                               max_length=30,
                               required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Nom',
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          })
                               )
    gender = forms.ChoiceField(choices=(('Man', 'Homme'), ('Woman', 'Femme')), widget=forms.Select(attrs={'class':'select_input input_authentication'}))


    email = forms.CharField(label="", max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          })
                               )
    city = forms.CharField(label="", max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Ville',
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          })
                           )
    password = forms.CharField(label="", max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Mot de passe',
                                                             'type' : "password",
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          }))

    password_again = forms.CharField(label="", max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Retapez votre mot de passe',
                                                             'type' : "password",
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          }))

    type_user = forms.ChoiceField(choices=(('Athlete', 'Athlete'), ('Coach', 'Coach')), widget=forms.Select(attrs={'class': 'select_input input_authentication'}))

    profil_picture = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'input_authentication'}))


class CompanyForm(forms.Form):
    name = forms.CharField(label="",
                               max_length=30,
                               required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Nom de l\'entreprise',
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          })
                               )
    date_creation = forms.DateField(widget = forms.SelectDateWidget(attrs={
                                                          'class': 'input_authentication',
                                                          })
                                    )

    category = forms.CharField(label="",
                               max_length=30,
                               required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Categorie',
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          })
                               )
    city = forms.CharField(label="",
                               max_length=30,
                               required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Ville',
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          })
                           )
    email = forms.CharField(label="", max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          })
                               )

    password = forms.CharField(label="", max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Mot de passe',
                                                             'type' : "password",
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          }))

    password_again = forms.CharField(label="", max_length=30, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Retapez votre mot de passe',
                                                             'type' : "password",
                                                          'style': 'width:150%;line-height: 1.9em;border-radius: 5px',
                                                          'class': 'input_authentication',
                                                          }))

    profil_picture = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'input_authentication'}))
