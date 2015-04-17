from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from .models import Post, Tag
import datetime


class PostTest(TestCase):
    ''' Testing Post model '''
    def setUp(self):
        #self.factory = RequestFactory()
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

    def test_string(self):
        ''' Tests string function '''
        self.assertTrue(str(self.test_post) == "Test Post")

    def test_edit(self):
        ''' Tests edit function '''
        retrieved_post = Post.objects.get(title="Test Post")
        retrieved_post.title = 'New Title'
        retrieved_post.save()
        self.assertEqual(retrieved_post.title, 'New Title')

    def test_unpublish(self):
        ''' Tests ability to test_unpublish posts '''
        retrieved_post = Post.objects.get(title="Test Post")
        retrieved_post.publish()
        self.assertNotEqual(retrieved_post.published_date, None)

        retrieved_post.unpublish()
        self.assertEqual(retrieved_post.published_date, None)

class TagTest(TestCase):
    ''' Tests tag functionality in application '''
    def setUp(self):
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

    def test_create_tags(self):
        ''' Tests functionality to create tags '''
        new_tag = Tag(word='New')
        new_tag.save()
        retrieve_tag = Tag.objects.get(word='New')
        self.assertEqual(retrieve_tag.word, 'New')

    def test_connect_tag(self):
        ''' Tests whether we can connect tag to model '''
        new_tag = Tag(word='New')
        new_tag.save()
        second_tag = Tag(word='Second')
        second_tag.save()
        self.test_post.tags = [new_tag, second_tag]
        self.test_post.save()
        retrieved_post = Post.objects.get(title="Test Post")
        self.assertEqual(len(retrieved_post.tags.all()), 2)



