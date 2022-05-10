from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = "gauravraj911@hotmail.com"
        password = "testpassword"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """Test if user email is normalised"""
        email = "gauravraj911@HOTMAIL.COM"
        password = "test123"
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,"pass123")   

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser("test@gmail.com", "test1234")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)         
