#!/usr/bin/python3
"""Tests all functions and return values of City Module"""
import unittest
from datetime import datetime as dt
import os
from models.city import City


class TestCity(unittest.TestCase):
    """Contains functions that are useful
    for testing the city module"""
    def setUp(self):
        """Initializes static values for test Citys"""
        self.city = City
        self.funcList = dir(self.city())

    def test_functionExists(self):
        """Checks if the City functions exist"""
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
        So we don't expect that from City
        """
        self.city(["hello", "man", "boy"])
        self.assertNotEqual(self.city().id, "hello")
        # checking that program doesn't initialize with *args

    def test_instance2(self):
        """Initializes with a dictionary and
        check if values initialized well"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        temp = self.city(**newIns)
        self.assertEqual(newIns["id"], temp.id)
        self.assertEqual(dt.fromisoformat(
            newIns["created_at"]), temp.created_at)
        self.assertEqual(dt.fromisoformat(
            newIns["updated_at"]), temp.updated_at)

    def test_instance3(self):
        """Checks the value type of attributes of class"""
        self.assertTrue(type(self.city().id), str)
        self.assertTrue(type(self.city().created_at), dt)
        self.assertTrue(type(self.city().updated_at), dt)

    def test_strRep(self):
        """Check the return value of __str__"""
        self.assertTrue(type(
            self.city().__str__()), str)

    def test_save1(self):
        """Checks the type value of updated_at after save function"""
        temp = self.city()
        temp.save()
        self.assertTrue(type(temp.updated_at), dt)

    def test_save2(self):
        """Checks if database exists after calling save function"""
        self.city().save()
        osList = os.listdir()
        self.assertTrue("file.json" in osList)

    def test_to_dict1(self):
        """Checks the return value of to_dict()"""
        self.assertTrue(type(self.city().to_dict()), dict)

    def test_to_dict2(self):
        """Checks if dictionary has the primary keys available"""
        data = [
            "id",
            "__class__",
            "created_at",
            "updated_at"
        ]
        for i in data:
            self.assertTrue(i in self.city().to_dict())

    def test_newValue(self):
        """Adds new Values in City"""
        temp = self.city()
        name = "My First Model"
        temp.name = name
        age = 89
        temp.age = age
        self.assertEqual(name, temp.name)
        self.assertEqual(age, temp.age)
        self.assertTrue("name" in temp.to_dict())
        self.assertTrue("age" in temp.to_dict())

    def test_class_attr(self):
        """Checks that each variable in module
        is first initialized with an empty string"""
        self.assertEqual(self.city().state_id, "")
        self.assertEqual(self.city().name, "")


if __name__ == "__main__":
    unittest.main()