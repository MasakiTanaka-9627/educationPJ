from django.test import TestCase
from .models import User

class UserAssertion(TestCase):
    def assertUserModel(self, actual_user, username, email, password):
        self.assertEqual(actual_user.username, username)
        self.assertEqual(actual_user.email, email)
        self.assertEqual(actual_user.password, password)

class UserModelTests(UserAssertion):
    def creating_a_user_and_saving(self, username=None, email=None, password=None):
        user = User()
        if username is not None:
            user.username = username
        if email is not None:
            user.email = email
        if user.password is not None:
            user.password = password

        user.save()

    def test_is_empty(self):
        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 0)

    def test_is_not_empty(self):
        self.creating_a_user_and_saving()
        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 0)

    def test_saving_and_retrieving_user(self):
        username, email, password = 'name', 'test@test.com', 'password'
        self.creating_a_user_and_saving(self, username, email, password)

        saved_users = User.objects.all()
        actual_user = saved_users[0]

        self.assertUserModel(actual_user, username, email, password)

