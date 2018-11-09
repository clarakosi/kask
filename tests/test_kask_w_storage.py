import unittest
import json
from kask import index
from semantic_version import Version


version = Version("1.0.0")
versioned = lambda p: "/v{}/{}".format(version.major, p.strip('/')).rstrip('/')
test_key = "ea183235b39a4feba8980ff1c1393f2c"
test_key_2 = "4460253a863a404da3d3ba28eb6cce89"

class TestKask(unittest.TestCase):
    def setUp(self):
        self.app = index.app.test_client()
        self.app.put(versioned("/%s" % test_key_2), data=json.dumps(dict(value="sample value")), content_type='application/json')

    def test_get(self):
        """404 Request"""
        response = self.app.get(versioned("/%s" % test_key))
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status, '404 NOT FOUND')
        self.assertEqual(data['detail'], 'The requested resource was not found')

        """200 Request"""
        response = self.app.get(versioned("/%s" % test_key_2))
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(data['value'], 'sample value')

    def test_set(self):
        """400 Request"""
        info = json.dumps(dict(value="another value"))
        response = self.app.put(versioned("/%s" % test_key), data=info)
        self.assertEqual(response.status, "400 BAD REQUEST")

        """201 Request"""
        response = self.app.put(versioned("/%s" % test_key), data=info, content_type='application/json')
        self.assertEqual(response.status, '201 CREATED')

    def test_delete(self):
        response = self.app.delete(versioned("/%s" % test_key_2))
        self.assertEqual(response.status, '204 NO CONTENT')
