"""
Tests for the user API.
"""
import sys
sys.path.append("..")
from core.models import User

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    """create and return a new user."""
    return User.objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """Test the public features of the user API such as registration
    which does not require authentication."""


    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successful."""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data) # type: ignore

    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists."""
        payload = {
            'email':'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an error is returned if password less than 5 characters."""
        payload = {
            'email':'test@example.com',
            'password': 'pq',
            'name': 'Test Name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = User.objects.filter(
            email = payload['email']
        ).exists()
        self.assertFalse(user_exists)