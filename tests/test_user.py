#!/usr/bin/python3
"""Tests all functions and return values of User Module"""
import unittest
from datetime import datetime as dt
import os
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """Initializes static values for test cases"""
        self.user = User
        self.funcList = dir(self.user())

    def test_functionExists(self):
        """Checks if the User functions exist"""
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
        So we don't expect that from User
        """
        self.user(["hello", "man", "boy"])
        self.assertNotEqual(self.user().id, "hello")
        # checking that program doesn't initialize with *args

    def test_instance2(self):
        """Initializes with a dictionary and
        check if values initialized well"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        temp = self.user(**newIns)
        self.assertEqual(newIns["id"], temp.id)
        self.assertEqual(dt.fromisoformat(
            newIns["created_at"]), temp.created_at)
        self.assertEqual(dt.fromisoformat(
            newIns["updated_at"]), temp.updated_at)

    def test_instance3(self):
        """Checks the value type of attributes of class"""
        self.assertTrue(type(self.user().id), str)
        self.assertTrue(type(self.user().created_at), dt)
        self.assertTrue(type(self.user().updated_at), dt)

    def test_strRep(self):
        """Check the return value of __str__"""
        self.assertTrue(type(
            self.user().__str__()), str)

    def test_save1(self):
        """Checks the type value of updated_at after save function"""
        temp = self.user()
        temp.save()
        self.assertTrue(type(temp.updated_at), dt)

    def test_save2(self):
        """Checks if database exists after calling save function"""
        self.user().save()
        osList = os.listdir()
        self.assertTrue("file.json" in osList)

    def test_to_dict1(self):
        """Checks the return value of to_dict()"""
        self.assertTrue(type(self.user().to_dict()), dict)

    def test_to_dict2(self):
        """Checks if dictionary has the primary keys available"""
        data = [
            "id",
            "__class__",
            "created_at",
            "updated_at"
        ]
        for i in data:
            self.assertTrue(i in self.user().to_dict())

    def test_newValue(self):
        """Adds new Values in User"""
        temp = self.user()
        name = "My First Model"
        temp.name = name
        password = "luckyd292"
        temp.password = password
        first_name = "Wiseman"
        last_name = "Jane"
        temp.first_name = first_name
        temp.last_name = last_name
        self.assertEqual(name, temp.name)
        self.assertEqual(password, temp.password)
        self.assertEqual(first_name, temp.first_name)
        self.assertEqual(last_name, temp.last_name)
        self.assertTrue("name" in temp.to_dict())
        self.assertTrue("password" in temp.to_dict())
        self.assertTrue("first_name" in temp.to_dict())
        self.assertTrue("last_name" in temp.to_dict())

    def test_class_attr(self):
        self.assertEqual(self.user().email, "")
        self.assertEqual(self.user().password, "")
        self.assertEqual(self.user().first_name, "")
        self.assertEqual(self.user().last_name, "")
