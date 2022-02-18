from unittest import TestCase
import http
import django.test
import AccountManager
import tests.utils as utils

class T(TestCase):

    # Set up
    def setUp(self):
        AccountManager.clear()


    # Create an account
    def createAccount(self, username, password):
        c = django.test.Client()
        resp = c.post("/register", {"username":username,"password":password})
        return resp


    # Test register
    # Given alice as a username
    # Doesn't already exist, returns true
    def test_registerCreateAccount(self):
        resp = self.createAccount("alice@example.com", "secret")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)


    # Different username
    # Give an error if username matches AND password is the same as others
    def test_registerNoDuplicate(self):
        resp = utils.createAccount("bob@example.com", "a_password")
        self.assertEqual(resp.status_code, http.HTTPStatus.OK)
        resp = utils.createAccount("bob@example.com", "some_garbage")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)


    # No username or password provided
    # If the user does not supply a username or password, report bad
    def test_registerMissingInfo(self):
        resp = utils.createAccountNoPassword("test@example.com")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)
        resp = utils.createAccountNoUsername("whats up")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)


    # Empty username or password
    # If the user provides an empty username and/or password, report bad
    def test_registerEmptyInfo(self):
        resp = utils.createAccount("desmond@gmail.com", "")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)
        resp = utils.createAccount("", "krabby patty")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)
        resp = utils.createAccount("", "")
        self.assertEqual(resp.status_code, http.HTTPStatus.BAD_REQUEST)