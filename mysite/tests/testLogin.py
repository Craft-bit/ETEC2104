"""from unittest import TestCase
import http
import django.test
import tests.utils as utils


class T(TestCase):
    decode() : 
    * difference between strings and bytes
        ** strings -> character data
        ** bytes -> binary data
    * we don't know what's coming back from a server
        ** could be text based
        ** could be an image
    * decode converts the resource from bytes into strings
    def test_notLoggedIn(self):
        # Runs as test, not actual browser
        c = django.test.Client()
        resp = c.get("/who")
        self.assertEqual("", resp.content.decode())

    def test_registerLogin(self):
        resp = utils.createAccount("desmond@foo.com", "gaming")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        uname = resp.client.get("/who").content.decode()
        self.assertEqual(uname, "desmond@foo.com")

    def test_registerDuplicatedAddress(self):
        # Assure we aren't logged in if address already exists
        resp = utils.createAccount("desmond@foo.com", "aPassword")
        uname = resp.client.get("/who").content.decode()
        self.assertNotEqual(uname, "desmond@foo.com")

    """