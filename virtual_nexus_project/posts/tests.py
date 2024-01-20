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

    def test_post_create(self):
        # log in user
        self.client.force_login(self.user)
        
        # check accessibility of page
        response = self.client.get(reverse('post-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create new post')

        # createing post
        post_data = {
            'title': 'test post123',
            'body': 'test post body'
        }
        response = self.client.post(reverse('post-create'), data=post_data)

        # check if the post was successfully created
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='test post123', body='test post body', author_id=self.user.id).exists())
    
