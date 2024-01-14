#!/usr/bin/python3
"""Tests all functions and return values of BaseModel Module"""
import unittest
from datetime import datetime as dt
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Initializes static values for test cases"""
        self.base = BaseModel
        self.funcList = dir(self.base())

    def test_functionExists(self):
        """Checks if the BaseModel functions exist"""
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
        self.base(["hello", "man", "boy"])
        self.assertNotEqual(self.base().id, "hello")
        # checking that program doesn't initialize with *args

    def test_instance2(self):
        """Initializes with a dictionary and
        check if values initialized well"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        temp = self.base(**newIns)
        self.assertEqual(newIns["id"], temp.id)
        self.assertEqual(dt.fromisoformat(
            newIns["created_at"]), temp.created_at)
        self.assertEqual(dt.fromisoformat(
            newIns["updated_at"]), temp.updated_at)

    def test_instance3(self):
        """Checks the value type of attributes of class"""
        self.assertTrue(type(self.base().id), str)
        self.assertTrue(type(self.base().created_at), dt)
        self.assertTrue(type(self.base().updated_at), dt)

    def test_strRep(self):
        """Check the return value of __str__"""
        self.assertTrue(type(
            self.base().__str__()), str)

    def test_save1(self):
        """Checks the type value of updated_at after save function"""
        temp = self.base()
        temp.save()
        self.assertTrue(type(temp.updated_at), dt)

    def test_save2(self):
        """Checks if database exists after calling save function"""
        self.base().save()
        osList = os.listdir()
        self.assertTrue("file.json" in osList)

    def test_to_dict1(self):
        """Checks the return value of to_dict()"""
        self.assertTrue(type(self.base().to_dict()), dict)

    def test_to_dict2(self):
        """Checks if dictionary has the primary keys available"""
        data = [
            "id",
            "__class__",
            "created_at",
            "updated_at"
        ]
        for i in data:
            self.assertTrue(i in self.base().to_dict())

    def test_newValue(self):
        """Adds new Values in BaseModel"""
        temp = self.base()
        name = "My First Model"
        temp.name = name
        age = 89
        temp.age = age
        self.assertEqual(name, temp.name)
        self.assertEqual(age, temp.age)
        self.assertTrue("name" in temp.to_dict())
        self.assertTrue("age" in temp.to_dict())


if __name__ == "__main__":
    unittest.main()
