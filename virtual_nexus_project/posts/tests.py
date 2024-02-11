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

    def test_post_search_not_found(self):
        """Testing what heppen if post not found
        """
        query_not_found = 'this query should not found '

        response = self.client.get(reverse('post-search'), {'q': query_not_found})

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, f'Searching results for "{ query_not_found }"')
        self.assertContains(response, 'Nothing has been found')

    def test_post_search_found(self):
        """Testing what heppen if post found
        """
        query = 'test post'

        response = self.client.get(reverse('post-search'), {'q': query})

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, f'Searching results for "{ query }"')
        self.assertContains(response, f'{query}')

    def test_post_edit(self):
        """Testing is posts editing correct 
        """

        self.client.force_login(self.user)
        url = reverse('post-edit', args=[self.post.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(url, {'title':'the best edited post ever',
                                          'body':'body of the best edited post ever'})
        self.assertEqual(response.status_code, 302)

        updated_post = Post.objects.get(id=self.post.id)
        
        self.assertEqual(updated_post.title, 'the best edited post ever')
        self.assertEqual(updated_post.body, 'body of the best edited post ever')