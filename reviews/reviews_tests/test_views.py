from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from reviews.models import (RecordCompany, Review, Genre, Artist,  Album)


class TestViewsLoggedOutUser(TestCase):

    def setUp(self):
        record = RecordCompany.objects.create(name='island')
        genre = Genre.objects.create(name='Dance')
        prodigy = Artist.objects.create(
            name='The Prodigy', date_formed='1992-01-01')
        fat_of_the_land = Album.objects.create(
            title='Fat of the land', year_of_release=1997,
            artist=prodigy, genre=genre,
            record_company=record)
        creator = User.objects.create(username='admin')
        creator.set_password('12345')
        creator.save()
        Review.objects.create(
            title='good', content='good', rating=10,
            album=fat_of_the_land, creator=creator)
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

    def test_user_can_log_in(self):
        logged_in = self.client.login(username='admin', password='12345')
        user = User.objects.get(username='admin')
        self.assertEqual(logged_in, True)
        self.assertTrue(user.is_authenticated)


class TestViewsLogggedInUser(TestCase):
    def setUp(self):
        record = RecordCompany.objects.create(name='island')
        genre = Genre.objects.create(name='Dance')
        prodigy = Artist.objects.create(
            name='The Prodigy', date_formed='1992-01-01')
        fat_of_the_land = Album.objects.create(
            title='Fat of the land', year_of_release=1997,
            artist=prodigy, genre=genre,
            record_company=record)
        creator = User.objects.create(username='admin')
        creator.set_password('12345')
        creator.save()
        Review.objects.create(
            title='good', content='good', rating=10,
            album=fat_of_the_land, creator=creator)
        self.client = Client()
        self.client.login(username='admin', password='12345')

    def test_logged_in_user_can_access_add_review(self):
        response = self.client.get('/add-review/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_review.html')

    def test_logged_in_user_can_logout(self):
        self.client.logout()
        response = self.client.get('/add-review/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/add-review/')

    def test_logged_in_user_can_add_a_genre(self):
        response = self.client.post('/add-genre', {'name': 'rap'})
        self.assertEqual(len(Genre.objects.all()), 2)
        self.assertTrue(Genre.objects.get(name='rap'))
        self.assertRedirects(response, reverse('add_review'))

    def test_logged_in_user_can_post_an_artist(self):
        response = self.client.post('/add-artist',
                                    {'name': '2pac',
                                     'date_formed': '1992-01-01',
                                     'website': 'www.2pac.com'})
        self.assertEqual(len(Artist.objects.all()), 2)
        self.assertEqual(response.status_code, 302)

    def test_logged_in_user_cannot_post_artist_without_all_fields(self):
        self.client.post('/add-artist',
                         {'name': '2pac',
                          'date_formed': '1992-01-01'})
        self.assertNotEqual(len(Artist.objects.all()), 2)

    def test_logged_in_user_can_post_a_record_company(self):
        response = self.client.post('/add-record-label',
                                    {'name': 'def-jam',
                                     'website': 'www.def-jam.com'})
        self.assertEqual(len(RecordCompany.objects.all()), 2)
        self.assertTrue(RecordCompany.objects.get(name='def-jam'))
        self.assertRedirects(response, reverse('add_review'))

    def test_logged_in_user_cannot_post_label_without_all_fields(self):
        self.client.post('/add-record-label',
                         {'name': 'def-jam'})
        self.assertEqual(len(RecordCompany.objects.all()), 1)

