from django.test import TestCase, Client
from django.urls import reverse
from .models import CustomUser, Employee


class EmployeeURLTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username="testuser",
            password="password",
            role="developer"
        )

    def test_home_url_access(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("employees:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "employees/home.html")

    def test_employee_list_requires_login(self):
        response = self.client.get(reverse("employees:employee_list"))
        self.assertNotEqual(response.status_code, 200)
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("employees:employee_list"))
        self.assertEqual(response.status_code, 200)
