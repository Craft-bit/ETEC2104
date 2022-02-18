"""
import AccountManager
from unittest import TestCase

class Tester(TestCase):

    @classmethod
    def setUp(self) -> None:
        global A
        A = AccountManager.AccountManager()
        A.addUser("alice", "qwerty")
        A.addUser("desmond", "deltarune")


    def test_verifyUser(self):
        self.assertFalse(A.verifyUser("bob", "s3cr3t"),
            "should return false if user doesn't exist")
        self.assertTrue(A.verifyUser("alice", "qwerty"),
            "should return true if user does exist and password matches")
        self.assertFalse(A.verifyUser("alice", "s3cr3t"),
            "should return false if password doesn't match")
        self.assertFalse(A.verifyUser("bob", "qwerty"),
            "should return false if user doesn't exist and password does match")
        # test for missing parameters
        self.assertRaises(Exception, A.verifyUser)
    

    def test_addUser(self):
        self.assertFalse(A.verifyUser("bob", "s3cr3t"))
        self.assertTrue(A.addUser("bob","s3cr3t"))
        self.assertTrue(A.verifyUser("bob", "s3cr3t"))


    def test_getUID(self):
        self.assertEqual(-1, A.getUID("joe"),
            "should return -1 if user doesn't exist")
        self.assertNotEqual(-1, A.getUID("alice"),
            "should return a number greater than 0 if user exists")
        self.assertNotEqual(A.getUID("joe"), A.getUID("alice"),
            "should compare two numbers and confirm both are not equal since user joe does not exist")
        self.assertNotEqual(A.getUID("desmond"), A.getUID("alice"),
            "should compare two numbers and confirm both are not equal since user desmond is a different user")

    def test_isAdmin(self):
        self.assertTrue(A.isAdmin("alice"),
            "should return true if user is administrator")
        self.assertFalse(A.isAdmin("desmond"),
            "should return false if user is administrator")
        self.assertFalse(A.isAdmin("joe"),
            "should return false if user is administrator")
        # test for missing paramaters
        self.assertRaises(Exception, A.isAdmin)

    def test_setAdmin(self):
        self.assertTrue(A.setAdmin(1, True),
            "should return true and clear admin flag since user is admin")
        self.assertTrue(A.setAdmin(2, False),
            "should return true and set admin flag since user is not admin")
        self.assertFalse(A.setAdmin(3, True),
            "should return false since user or ID does not exist")
        # test for missing paramaters
        self.assertRaises(Exception, A.setAdmin)
"""
