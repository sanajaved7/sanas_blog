from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from .models import Post, Tag
import datetime


class PostTest(TestCase):
    ''' Testing Post model '''
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username = 'sana',
            email='sjaved@umd.edu',
            password='password')

    def test_save(self):
        '''Tests simple save case'''
        test_post = Post(
            author=self.user,
            title="Test Post",
            text="This is a test post.",
            created_date = datetime.date.today(),
            published_date = datetime.date.today()
            )
        test_post.save()
