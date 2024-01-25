from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import UserProfile

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser123',
            email='testuseremail@gmail.com',
            password='verysecurepassword123',   
        )
        self.user_profile = UserProfile.objects.get_or_create(
            user=self.user,
            defaults={'bio': 'Test bio.'}
        )
        

    def test_user_profile_page(self):

        #set up for this test
        self.client.login(email='testuseremail@gmail.com', password='verysecurepassword123')
        url = reverse('profile')
        response = self.client.get(url)
        
        #exacly test
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')
        self.assertContains(response, 'Username: testuser123', html=True)
        self.assertContains(response, '<h2>User Profile</h2>', html=True)
        self.assertNotContains(response, '<form method="post" enctype="multipart/form-data">', html=True)

    def test_user_profile_for_others(self):
        
        url = reverse('profile-detail', kwargs={'pk':self.user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile_for_others_users.html')
        self.assertContains(response, '<h2>User Profile</h2>', html=True)
