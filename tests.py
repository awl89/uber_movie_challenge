import unittest

import urllib2
import json

from app import *
from app import models
from app import views


class TestDatabaseConsistency(unittest.TestCase):

    def setUp(self):
        configure_app("test1")
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index_page_consistency(self):
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_title_consistency(self):
        resp = self.app.get('/search_title', query_string=dict(title='American Graffiti'), follow_redirects=False)
        self.assertEqual(resp.status_code, 200)

    def test_title_inconsistency(self):
        resp = self.app.get('/search_title', query_string=dict(title='asdf'), follow_redirects=False)
        self.assertEqual(resp.status_code, 404)

    def test_production_year_consistency(self):
        resp = self.app.get('/search_title', query_string=dict(title='Bullit'), follow_redirects=False)
        resp_json = json.loads(resp.data)
        year = resp_json['results'][0]['year']
        self.assertEqual(year, 1968)

    def test_location_consistency(self):
        resp = self.app.get('/search_title', query_string=dict(title='Cherish'), follow_redirects=False)
        resp_json = json.loads(resp.data)
        location = resp_json['results'][0]['location']
        self.assertEqual(location, '387 Fair Oaks at 25th Street')

    def test_distributor_consistency(self):
        resp = self.app.get('/search_title', query_string=dict(title='Greed'), follow_redirects=False)
        resp_json = json.loads(resp.data)
        distributor = resp_json['results'][0]['distributor']
        self.assertEqual(distributor, 'Metro-Goldwyn-Mayer (MGM)')

    def test_director_consistency(self):
        resp = self.app.get('/search_title', query_string=dict(title='Heart Beat'), follow_redirects=False)
        resp_json = json.loads(resp.data)
        director = resp_json['results'][0]['director']
        self.assertEqual(director, 'John Byrum')

    def test_writer_consistency(self):
        resp = self.app.get('/search_title', query_string=dict(title='Herbie Rides Again'), follow_redirects=False)
        resp_json = json.loads(resp.data)
        writer = resp_json['results'][0]['writer']
        self.assertEqual(writer, 'Bill Walsh')

    def test_actor1_consistency(self):
        resp = self.app.get('/search_title', query_string=dict(title='Junior'), follow_redirects=False)
        resp_json = json.loads(resp.data)
        actor1 = resp_json['results'][0]['actor1']
        self.assertEqual(actor1, 'Arnold Schwarzenegger')

    def test_number_of_occurrences(self):
        resp = self.app.get('/search_title', query_string=dict(title='Basic Instinct'), follow_redirects=False)
        resp_json = json.loads(resp.data)
        num_of_occurrences = len(resp_json['results'])
        self.assertEqual(num_of_occurrences, 13)


class CreateMovieTests(unittest.TestCase):

    def setUp(self):
        configure_app("test2")
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_missing_title(self):
        rv = self.app.post('/create_movie', data=dict(title="D", year=1964, location="Chinatown", director="Stanley Kubrick") )
        assert "<strong>'<label for=\"title\">Title</label>' </strong> - Field must be between 2 and 50 characters long." in rv.data

    def test_missing_location(self):
        rv = self.app.post('/create_movie', data=dict(title="Dr. Strangelove", year=1964, location="", director="Stanley Kubrick") )
        assert "<strong>'<label for=\"location\">Location</label>' </strong> - This field is required." in rv.data
    

    def test_missing_director(self):
        rv = self.app.post('/create_movie', data=dict(title="Dr. Strangelove", year=1964, location="Chinatown", director="") )
        assert "<strong>'<label for=\"director\">Director</label>' </strong> - This field is required." in rv.data

    def test_created_movie_sucessfully(self):
        rv = self.app.post('/create_movie', data=dict(title="Dr. Strangelove", year=1964, location="Chinatown", director="Stanley Kubrick") )
        assert rv.status_code == 302
        assert '/' in rv.headers['Location']

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDatabaseConsistency))
    suite.addTest(unittest.makeSuite(CreateMovieTests))
    return suite

def test_runner():
    runner = unittest.TextTestRunner()
    runner.run(test_suite())

if __name__ == '__main__':
    test_runner()