from django.test import TestCase
from .models import User

class UserModelTests(TestCase):
    def test_is_empty(self):
        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 0)

    def test_is_not_empty(self):
        user = User()
        user.save()
        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 1)

    def test_saving_and_retrieving_user(self):
        first_user = User()
        username, email, password = 'name', 'test@test.com', 'password'
        first_user.username = username
        first_user.email = email
        first_user.password = password
        first_user.save()

        saved_users = User.objects.all()
        actual_user = saved_users[0]

        self.assertEqual(actual_user.username, username)
        self.assertEqual(actual_user.email, email)
        self.assertEqual(actual_user.password, password)