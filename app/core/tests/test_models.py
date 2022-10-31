"""
Tests for models.
"""
from ..models import User, Recipe
from django.test import TestCase
from decimal import Decimal


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = User.objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_user_emails(self):
        """ Test if email is normalized for new users """
        sample_emails = [
            ['test@EXAMPLE.com', 'test@example.com'],
            ['Test2@EXAMPLE.com', 'Test2@example.com'],
            ['TEST@EXAMPLE.com', 'TEST@example.com'],
            ['Test3@example.COM', 'Test3@example.com'],
        ]

        for email, expected in sample_emails:
            user = User.objects.create_user(email, 'sample@123')
            self.assertEqual(user.email, expected)

    def test_new_users_without_email(self):
        """ Test if new users added without email address and raise error if so""" # noqa
        with self.assertRaises(ValueError):
            User.objects.create_user('', 'sample@123')

    def test_create_super_user(self):
        """ Test creation of superuser """
        user = User.objects.create_superuser(
            'test@example.com',
            'test@1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creation of recipe."""
        user = User.objects.create_user(
            'test@example.com',
            'test@1234'
        )

        recipe = Recipe.objects.create(
            user=user,
            title='Sample recipe',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description',
        )

        self.assertEqual(str(recipe), recipe.title)
