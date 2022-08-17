"""
Any or all tests applyed to model classes
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email(self):
        """testing usr creation with email"""
        email = 'test@gmail.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        # checking password through hashing system
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test email normalization"""
        sample_email = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Gmail.com', 'Test2@gmail.com'],
            ['TEST3@GMAIL.COM', 'TEST3@gmail.com'],
            ['test4@gmail.com', 'test4@gmail.com']
        ]
        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """test that creating a user without email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample123')

    def test_create_superuser(self):
        """test creating superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
