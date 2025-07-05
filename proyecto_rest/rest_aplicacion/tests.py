from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import BlogPost

class BlogPostTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse('blogpost-list')
        self.data = {
            'title': 'Test Post',
            'content': 'This is a test content.',
            'author': self.user.id
        }
    def test_create_blogpost(self):
        url = reverse('blogpost-list')
        data = {'title': 'Test Post', 'content': 'This is a test content.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 1)
        self.assertEqual(BlogPost.objects.get().title, 'Test Post')

        