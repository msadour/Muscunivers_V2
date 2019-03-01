from .form import search_form, publication_form
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "muscunivers_project.settings")


data = {'in_maintenance': False,
        'search_form': search_form.SearchForm(),
        'status_form': publication_form.StatusForm(),
        'status_form_wall': publication_form.StatusToWallUserForm(),
        'comment_form': publication_form.CommentForm(),
        'my_profil': None
        }