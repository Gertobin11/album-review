from django.contrib.auth.models import User
from django.test import TestCase
from reviews.models import Album, Genre, Artist, RecordCompany, Review


class GenreTestCase(TestCase):
    def setUp(self):
        Genre.objects.create(name='hiphop')

    def test_genre_exists(self):
        hiphop = Genre.objects.get(name='hiphop')
        self.assertEqual(hiphop.name, 'hiphop')

    def test_create_object(self):
        Genre.objects.create(name='rock')
        self.assertEqual(len(Genre.objects.all()), 2)

    def test_update_an_object(self):
        object_one = Genre.objects.get(name='hiphop')
        object_one.name = 'dance'
        self.assertEqual(object_one.name, 'dance')

    def test_delete_a_genre_object(self):
        object_two = Genre.objects.get(name='hiphop')
        object_two.delete()
        self.assertEqual(len(Genre.objects.all()), 0)

    def test__genre_model_string(self):
        hiphop = Genre.objects.get(name='hiphop')
        self.assertEqual(str(hiphop), 'hiphop')


class ArtistTestCase(TestCase):
    def setUp(self):
        Artist.objects.create(name='Audioslave', date_formed='1989-01-01',
                              website='www.test.com')

    def test_get_object(self):
        band = Artist.objects.get(name='Audioslave')
        self.assertEqual(band.website, 'www.test.com')

    def test_create_an_artist(self):
        Artist.objects.create(name='test', date_formed='1999-01-01')
        self.assertEqual(len(Artist.objects.all()), 2)

    def test_can_update_name(self):
        audioslve = Artist.objects.get(name='Audioslave')
        audioslve.name = 'Soundgarden'
        self.assertEqual(audioslve.name, 'Soundgarden')

    def test_can_update_date_formed(self):
        audioslve = Artist.objects.get(name='Audioslave')
        audioslve.date_formed = '1998-01-01'
        self.assertEqual(audioslve.date_formed, '1998-01-01')

    def test_delete_an_artist_object(self):
        band = Artist.objects.get(name='Audioslave')
        band.delete()
        self.assertEqual(len(Artist.objects.all()), 0)

    def test_add_a_website_value(self):
        test = Artist.objects.create(name='test', date_formed='1999-01-01')
        test.website = 'www.test2.com'
        self.assertEqual(test.website, 'www.test2.com')

    def test_genre_model_string(self):
        artist = Artist.objects.get(name='Audioslave')
        self.assertEqual(str(artist), 'Audioslave')


class RecordCompanyTestCase(TestCase):
    def setUp(self):
        RecordCompany.objects.create(name='Death-Row',
                                     website='www.deathrow.com')

    def test_get_record_company(self):
        suge = RecordCompany.objects.get(name='Death-Row')
        self.assertEqual(suge.name, 'Death-Row')

    def test_create_a_record_company_object(self):
        RecordCompany.objects.create(website='test')
        self.assertEqual(len(RecordCompany.objects.all()), 2)

    def test_edit_a_recored_compay_object(self):
        death_row = RecordCompany.objects.get(name="Death-Row")
        death_row.website = "www.death-row.com"
        self.assertEqual(death_row.website, 'www.death-row.com')

    def test_delete_a_record_company_object(self):
        death_row = RecordCompany.objects.get(name="Death-Row")
        death_row.delete()
        self.assertEqual(len(RecordCompany.objects.all()), 0)

    def test_add_a_value_to_record_company_object(self):
        death_row = RecordCompany.objects.get(name="Death-Row")
        death_row.rating = 5
        self.assertEqual(death_row.rating, 5)

    def test_record_company_model_string(self):
        label = RecordCompany.objects.get(name='Death-Row')
        self.assertEqual(str(label), 'Death-Row')


class AlbumTestCase(TestCase):
    def setUp(self):
        record = RecordCompany.objects.create(name='island')
        genre = Genre.objects.create(name='Dance')
        prodigy = Artist.objects.create(name='The Prodigy',
                                        date_formed='1992-01-01')
        Album.objects.create(title='Fat of the land', year_of_release=1997,
                             artist=prodigy, genre=genre,
                             record_company=record)
        Album.objects.create(title='Music for the jilted generation',
                             year_of_release=1995,
                             artist=prodigy, genre=genre,
                             record_company=record)

    def test_get_album_object(self):
        album = Album.objects.get(title='Fat of the land')
        self.assertEqual(album.title, 'Fat of the land')

    def test_get_all_objects(self):
        albums = Album.objects.all()
        self.assertEqual(len(albums), 2)

    def test_create_a_new_album(self):
        artist = Artist.objects.create(name='2pac',
                                       date_formed='1992-01-01')
        record = RecordCompany.objects.create(name='death-row')
        genre = Genre.objects.create(name='Rap')
        Album.objects.create(title='All Eyez On Me', year_of_release=1996,
                             artist=artist, genre=genre,
                             record_company=record)
        self.assertEqual(len(Album.objects.all()), 3)

    def test_can_edit_an_album_object(self):
        fat_of_the_land = Album.objects.get(title='Fat of the land')
        fat_of_the_land.year_of_release = 1997
        self.assertEqual(fat_of_the_land.year_of_release, 1997)

    def test_change_fk_relation(self):
        interscope = RecordCompany.objects.create(name='Interscope')
        fat_of_the_land = Album.objects.get(title='Fat of the land')
        fat_of_the_land.record_company = interscope
        self.assertEqual(fat_of_the_land.record_company, interscope)

    def test_can_delete_album_object(self):
        fat_of_the_land = Album.objects.get(title='Fat of the land')
        fat_of_the_land.delete()
        self.assertEqual(len(Album.objects.all()), 1)

    def test_album_model_string(self):
        album = Album.objects.get(year_of_release=1997)
        self.assertEqual(str(album), 'Fat of the land')


class ReviewTestCase(TestCase):
    def setUp(self):
        record = RecordCompany.objects.create(name='island')
        genre = Genre.objects.create(name='Dance')
        prodigy = Artist.objects.create(name='The Prodigy',
                                        date_formed='1992-01-01')
        fat_of_the_land = Album.objects.create(title='Fat of the land',
                                               year_of_release=1997,
                                               artist=prodigy, genre=genre,
                                               record_company=record)
        creator = User.objects.create(username='admin')
        Review.objects.create(title='good', content='good', rating=10,
                              album=fat_of_the_land, creator=creator)

    def test_get_a_review_object(self):
        review = Review.objects.get(title='good')
        self.assertEqual(review.content, 'good')

    def test_create_a_new_review(self):
        album = Album.objects.get(title='Fat of the land')
        user = User.objects.get(username='admin')
        Review.objects.create(title='ok', content='ok', rating=11,
                              album=album, creator=user)
        self.assertEqual(len(Review.objects.all()), 2)

    def test_can_edit_a_review(self):
        review = Review.objects.get(title='good')
        review.content = 'very good'
        self.assertEqual(review.content, 'very good')

    def test_can_delete_review(self):
        review = Review.objects.get(title='good')
        review.delete()
        self.assertEqual(len(Review.objects.all()), 0)

    def test_review_model_string(self):
        review = Review.objects.get(title='good')
        self.assertEqual(str(review), 'Fat of the land reviewed by admin')
