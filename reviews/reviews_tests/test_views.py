from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from reviews.models import (RecordCompany, Review, Genre, Artist,  Album)


class TestViewsLoggedOutUser(TestCase):

    def setUp(self):
        self.record = RecordCompany.objects.create(name='island')
        self.genre = Genre.objects.create(name='Dance')
        self.prodigy = Artist.objects.create(
            name='The Prodigy', date_formed='1992-01-01')
        self.fat_of_the_land = Album.objects.create(
            title='Fat of the land', year_of_release=1997,
            artist=self.prodigy, genre=self.genre,
            record_company=self.record)
        self.creator = User.objects.create(username='admin')
        self.review = Review.objects.create(
            title='good', content='good', rating=10,
            album=self.fat_of_the_land, creator=self.creator)
        self.client = Client()

    def test_index_get(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_reviews_get(self):
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list.html')

    def test_albums_get(self):
        response = self.client.get(reverse('album_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'album_list.html')

    def test_review_detail_get(self):
        response = self.client.get(reverse('review', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review.html')

    def test_album_detail_get(self):
        response = self.client.get(reverse('album_view', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'album_view.html')

    def test_search_view(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')

    def test_logged_out_user_cannot_access_add_review_view(self):
        response = self.client.get(reverse('add_review'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/add-review/')

    def test_logged_out_user_cannot_post_review(self):
        album = Album.objects.get(title='Fat of the land')
        user = User.objects.get(username='admin')
        response = self.client.post('/add-review', {
            'album': album,
            'creator': user,
            'title': 'test',
            'content': 'test',
            'rating': 5
        })
        self.assertEqual(response.status_code, 301)
        self.assertEqual(len(Review.objects.all()), 1)

