from django.test import TestCase

from .models import User


class HomeTest(TestCase):

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get("/login/")

        self.assertEqual(response.status_code, 200)

    def test_login(self):
        User.objects.create_user(email="test@example.com", password="TestPass123")

        logged_in = self.client.login(email="test@example.com", password="TestPass123")

        self.assertTrue(logged_in)

    def test_user_role(self):
        user = User.objects.create_user(
            email="bronze@example.com", password="TestPass123", role="bronze"
        )

        self.assertEqual(user.role, "bronze")
