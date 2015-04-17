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
        self.test_post = Post(
            author=self.user,
            title="Test Post",
            text="This is a test post.",
            created_date = datetime.datetime(2014,12,27)
            )
        self.test_post.save()

    def test_retrieval(self):
        '''Tests whether we can retrieve a saved post'''
        retrieved_post = Post.objects.get(title="Test Post")
        self.assertEqual(retrieved_post.author.username, "sana")
        self.assertEqual(retrieved_post.author.email, "sjaved@umd.edu")
        self.assertEqual(retrieved_post.text, "This is a test post.")
        self.assertEqual(retrieved_post.created_date,
            datetime.datetime(2014,12,27))

    def test_publish(self):
        ''' Test simple publish case '''
        self.assertEqual(self.test_post.published_date, None)
        self.test_post.publish()
        self.assertNotEqual(self.test_post.published_date, None)




