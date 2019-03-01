import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "muscunivers_project.settings")
import django ; django.setup()
from django.db.models import Q
from .features import *


class TestCheckErrorUser:
    def setup_method(self):
        self.good_user = "usertest"
        self.wrong_user = "c"
        self.good_mail = "usertest@gmail.com"
        self.wrong_mail = "wrong"
        self.good_password = "azerty"
        self.wrong_password = "s"
        self.good_password_again = "azerty"
        self.wrong_password_again = "qwerty"

    def test_user(self):
        check = check_error_user(self.wrong_user, self.good_mail, self.good_password, self.good_password_again)
        assert len(check) > 0

    def test_mail(self):
        check = check_error_user(self.good_user, self.wrong_mail, self.good_password, self.good_password_again)
        assert len(check) > 0

    def test_password(self):
        check_wrong_password = check_error_user(self.wrong_user, self.good_mail, self.wrong_password, self.wrong_password_again)
        check_different_password = check_error_user(self.wrong_user, self.good_mail, self.good_password, self.wrong_password_again)
        assert len(check_wrong_password) > 0 and len(check_different_password) > 0

    def test_mix_errors(self):
        check_all_good = check_error_user(self.good_user, self.good_mail, self.good_password, self.good_password_again)
        check_all_wrong =  check_error_user(self.wrong_user, self.wrong_mail, self.wrong_password, self.wrong_password_again)
        assert len(check_all_good) == 0 and len(check_all_wrong) > 0


class TestPublishMessage:
    def setup_method(self):
        self.message = "statusTest"
        self.author = User.objects.get(username='msadour')

    def test_publication(self):
        error = False
        try:
            publish_message(self.author, self.message)
        except:
            error = True

        assert error == False

    def test_reset_data(self):
        status = Status.objects.filter(Q(message=self.message) & Q(author=self.author))
        for one_status in status:
            get_object_user(self.author).status.remove(one_status)
            one_status.delete()


# class CommentTest:
#     def setup_method(self):
#         self.comment = "d'accord"
#         self.author = User.objects.get(username='msadour')
#         self.receiver = User.objects.get(username='jdupont')
#
#     def test_comment(self):
#         pass


class TestGetObjectUser:
    def setup_method(self):
        self.athlete = get_object_user(26)
        self.coach = get_object_user(29)
        self.company = get_object_user(30)
        self.wrong = get_object_user(0)

    def test_get_user(self):
        assert self.athlete.get_type_user() == 'Athlete' and self.coach.get_type_user() == 'Coach' \
               and self.company.get_type_user() == 'Company' and self.wrong is None


class TestSearch:
    def setup_method(self):
        self.search_all_good = "j"
        self.search_all_wrong = "cfdkjbjgbhjhj"
        self.search_athlete_good = "msadour"
        self.search_athlete_wrong = "cfdkjbjgbhjhj"
        self.search_coach_good = "lgerard"
        self.search_coach_wrong = "cfdkjbjgbhjhj"
        self.search_company_good = "ocfitness"
        self.search_company_wrong = "cfdkjbjgbhjhj"
        self.current_user = get_object_user(27)

    def test_search_all(self):
        search_good = search(self.current_user, self.search_all_good)
        search_wrong_athlete, search_wrong_coach, search_wrong_company = search(self.current_user, self.search_all_wrong)
        assert len(search_good) > 0 and len(search_wrong_athlete) == 0 and len(search_wrong_coach) == 0 and len(search_wrong_company) == 0

    def test_search_athlete(self):
        search_good = search(self.current_user, self.search_athlete_good, 'Athlete')
        search_wrong = search(self.current_user, self.search_athlete_wrong, 'Athlete')
        assert len(search_good) > 0 and len(search_wrong) == 0

    def test_search_coach(self):
        search_good = search(self.current_user, self.search_coach_good, 'Coach')
        search_wrong = search(self.current_user, self.search_coach_wrong, 'Coach')
        assert len(search_good) > 0 and len(search_wrong) == 0

    def test_search_company(self):
        search_good = search(self.current_user, self.search_company_good, 'Company')
        search_wrong = search(self.current_user, self.search_company_wrong, 'Company')
        assert len(search_good) > 0 and len(search_wrong) == 0


class TestConnectionUser:
    def setup_method(self):
        self.good_user = "msadour"
        self.wrong_user = "frnijgbre"
        self.good_password = "azerty"
        self.wrong_password = "wrong"

    def test_connection(self):
        good_user_wrong_password = connection_user(self.good_user, self.wrong_password)['errors']
        good_user_good_password = connection_user(self.good_user, self.good_password)['errors']
        wrong_user = connection_user(self.wrong_user, self.good_password)['errors']
        wrong_all = connection_user(self.wrong_user, self.wrong_password)['errors']

        assert len(good_user_good_password) == 0 and len(good_user_wrong_password) > 0 and len(wrong_user) > 0 and len(wrong_all) > 0
#
#
# # class InscriptionUserTest:
# #     def setup_method(self):
# #         pass
# #
# #     def test_inscription_athlete(self):
# #         pass
# #
# #     def test_inscription_coach(self):
# #         pass
# #
# #     def test_inscription_company(self):
# #         pass
#
#


class TestSendMessageToContact:
    def setup_method(self):
        self.message = "mesagetest"
        self.author = User.objects.get(username='msadour')
        self.receiver = User.objects.get(username='jdupont')

    def test_message(self):
        error = False
        try:
            send_message_to_contact(get_object_user(self.author), get_object_user(self.receiver), self.message)
        except:
            error = True

        assert error is False

    def test_reset_data(self):
        messages = Message.objects.filter(Q(message=self.message) & Q(author=self.author))
        for message in messages:
            message.delete()
        assert True


class TestCreateService:
    def setup_method(self):
        self.coaching = {'name' : 'testcoaching', 'price' : 1, 'description' : 'testcoaching'}
        self.product = {'name' : 'testproduct', 'price' : 1, 'description' : 'testproduct', 'weblink' : 'https://google.fr'}
        self.coach = get_object_user(29)
        self.company = get_object_user(30)

    def test_create_coaching(self):
        try:
            create_service('coaching', self.coaching, self.coach)
        except:
            assert False
        else:
            coachings = Coaching.objects.filter(name='testcoaching')
            for coaching in coachings:
                self.coach.coachings.remove(coaching)
                coaching.delete()
            assert True

    def test_create_product(self):
        try:
            create_service('product', self.product, self.company)
        except:
            assert False
        else:
            products = Product.objects.filter(name='testproduct')
            for product in products:
                self.company.products.remove(product)
                product.delete()
            assert True


class TestUpdateProfilData:
    def setup_method(self):
        self.form_company = {'password': '', 'category': '', 'email': '', 'place': '', 'name': 'usertest', 'password_again': '', 'date_creation': ''}
        self.form_coach = {'password': '', 'email': '', 'password_again': '', 'first_name': '', 'last_name': '', 'user_name': 'usertestcoach', 'place': ''}
        self.form_athlete = {'password': '', 'email': '', 'password_again': '', 'first_name': '', 'last_name': '', 'user_name': 'usertestathlete', 'place': ''}
        self.user_profil_company = get_object_user(30)
        self.user_profil_coach = get_object_user(29)
        self.user_profil_athlete = get_object_user(27)

    def test_update_athlete(self):
        update_profil_data(self.user_profil_athlete, self.form_athlete)
        assert self.user_profil_athlete.user.username == 'usertestathlete'

    def test_update_coach(self):
        update_profil_data(self.user_profil_coach, self.form_coach)
        assert self.user_profil_coach.user.username == 'usertestcoach'

    def test_update_company(self):
        update_profil_data(self.user_profil_company, self.form_company)
        assert self.user_profil_company.user.username == 'usertest'

    def test_reset_data(self):
        self.user_profil_company.user.username = 'openclassrooms'
        self.user_profil_company.name = 'openclassrooms'
        self.user_profil_company.user.save()
        self.user_profil_company.save()
        self.user_profil_coach.user.username = 'lgerard'
        self.user_profil_coach.user.save()
        self.user_profil_coach.save()
        self.user_profil_athlete.user.username = 'msadour'
        self.user_profil_athlete.user.save()
        self.user_profil_athlete.save()
        assert True