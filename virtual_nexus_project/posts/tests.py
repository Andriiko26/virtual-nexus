from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from .models import Post



class PostTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='testuser123',
            email='testuseremail@gmail.com',
            password='verysecurepassword123',   
        )
        self.post = Post.objects.create(
            title='the best post ever',
            body='body of the best post ever',
            author=self.user,
        )

    def test_post_listing(self):

        self.assertEqual(f'{self.post.title}', 'the best post ever')
        self.assertEqual(f'{self.post.body}', 'body of the best post ever')
        self.assertEqual(f'{self.post.author}', f'{self.user}')
    
    def test_post_listing_view(self):

        response = self.client.get(reverse('post-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/index.html')
    
