import unittest
import json
from kask import index

versioned = index.versioned
test_key = "ea183235b39a4feba8980ff1c1393f2c"
test_key_2 = "4460253a863a404da3d3ba28eb6cce89"


class TestKask(unittest.TestCase):
    def setUp(self):
        self.app = index.app.test_client()
        self.app.put(versioned("/%s" % test_key_2),
                     data=json.dumps(dict(value="sample value")),
                     content_type='application/json')

    def tearDown(self):
        index.store.values = {}

    def test_get_missing(self):
        """Fetches a non-existent key, and expects a 404"""
        response = self.app.get(versioned("/%s" % test_key))
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status, '404 NOT FOUND')
        self.assertEqual(data['detail'], 'The requested resource was not found')

    def test_get(self):
        """Fetches a key that exists, and expects a 200"""
        response = self.app.get(versioned("/%s" % test_key_2))
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(data['value'], 'sample value')

    def test_set_bad_request(self):
        """Sets a key with missing content type, and expects 400"""
        info = json.dumps(dict(value="another value"))
        response = self.app.put(versioned("/%s" % test_key), data=info)
        self.assertEqual(response.status, "400 BAD REQUEST")

    def test_set(self):
        """Sets a key, and expects a 201"""
        info = json.dumps(dict(value="another value"))
        response = self.app.put(versioned("/%s" % test_key),
                                data=info, content_type='application/json')
        self.assertEqual(response.status, '201 CREATED')

    def test_delete(self):
        """Deletes a key from storage, and expects a 204"""
        response = self.app.delete(versioned("/%s" % test_key_2))
        self.assertEqual(response.status, '204 NO CONTENT')
