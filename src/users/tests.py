from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy, reverse


class LoginTest(TestCase):
    test_username = 'test_user'
    test_password = 'test_pass'

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username=cls.test_username,
            password=cls.test_password
        )

    def test_accessibility(self):
        resp = self.client.get(reverse_lazy('users:login'))
        self.assertEqual(resp.status_code, 200)

    def test_use_correct_template(self):
        resp = self.client.get(reverse_lazy('users:login'))
        self.assertTemplateUsed(resp, 'users/auth/login.html')

    def test_login_if_correct_username_and_pass(self):
        credentials = {
            'username': self.test_username,
            'password': self.test_password
        }
        response = self.client.post(reverse('users:login'), credentials)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(response.url)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_dont_login_if_not_correct_username_and_pass(self):
        credentials = {
            'username': 'not_correct',
            'password': 'not_correct'
        }
        response = self.client.post(reverse('users:login'), credentials)

        self.assertEqual(response.status_code, 200)

        self.assertIsNotNone(response.context['form'].errors)
        self.assertFalse(response.context['user'].is_authenticated)
