#!/usr/bin/python3
"""Tests all functions and return values of Review Module"""
import unittest
from datetime import datetime as dt
import os
from models.review import Review


class TestReview(unittest.TestCase):
	"""Contains functions that are useful
    for testing the Review module"""
    def setUp(self):
        """Initializes static values for test Reviews"""
        self.review = Review
        self.funcList = dir(self.review())

    def test_functionExists(self):
        """Checks if the Review functions exist"""
        modelList = [
            "__init__",
            "__str__",
            "save",
            "to_dict"
        ]
        for i in modelList:
            self.assertTrue(i in self.funcList)

    def test_instances1(self):
        """
        Checking that program doesn't initialize with *args
        This is because we don't make use of *args throughout the program
        So we don't expect that from Review
        """
        self.review(["hello", "man", "boy"])
        self.assertNotEqual(self.review().id, "hello")
        # checking that program doesn't initialize with *args

    def test_instance2(self):
        """Initializes with a dictionary and
        check if values initialized well"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        temp = self.review(**newIns)
        self.assertEqual(newIns["id"], temp.id)
        self.assertEqual(dt.fromisoformat(
            newIns["created_at"]), temp.created_at)
        self.assertEqual(dt.fromisoformat(
            newIns["updated_at"]), temp.updated_at)

    def test_instance3(self):
        """Checks the value type of attributes of class"""
        self.assertTrue(type(self.review().id), str)
        self.assertTrue(type(self.review().created_at), dt)
        self.assertTrue(type(self.review().updated_at), dt)

    def test_strRep(self):
        """Check the return value of __str__"""
        self.assertTrue(type(
            self.review().__str__()), str)

    def test_save1(self):
        """Checks the type value of updated_at after save function"""
        temp = self.review()
        temp.save()
        self.assertTrue(type(temp.updated_at), dt)

    def test_save2(self):
        """Checks if database exists after calling save function"""
        self.review().save()
        osList = os.listdir()
        self.assertTrue("file.json" in osList)

    def test_to_dict1(self):
        """Checks the return value of to_dict()"""
        self.assertTrue(type(self.review().to_dict()), dict)

    def test_to_dict2(self):
        """Checks if dictionary has the primary keys available"""
        data = [
            "id",
            "__class__",
            "created_at",
            "updated_at"
        ]
        for i in data:
            self.assertTrue(i in self.review().to_dict())

    def test_newValue(self):
        """Adds new Values in Review"""
        temp = self.review()
        text = "This is one of the best models"
        temp.text = text
        place_id = temp.id
        temp.place_id = place_id
        user_id = temp.id
        temp.user_id = user_id
        self.assertEqual(text, temp.text)
        self.assertEqual(place_id, temp.place_id)
        self.assertEqual(user_id, temp.user_id)
        self.assertTrue("text" in temp.to_dict())
        self.assertTrue("place_id" in temp.to_dict())
        self.assertTrue("user_id" in temp.to_dict())

    def test_class_attr(self):
		"""Checks the inital value of vaiables"""
        self.assertEqual(self.review().text, "")
        self.assertEqual(self.review().place_id, "")
        self.assertEqual(self.review().user_id, "")


if __name__ == "__main__":
    unittest.main()