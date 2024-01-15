#!/usr/bin/python3
"""Tests all functions and return values of Place Module"""
import unittest
from datetime import datetime as dt
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """Contains functions that are useful
    for testing the place module"""
    def setUp(self):
        """Initializes static values for test Places"""
        self.place = Place
        self.funcList = dir(self.place())

    def test_functionExists(self):
        """Checks if the Place functions exist"""
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
        So we don't expect that from Place
        """
        self.place(["hello", "man", "boy"])
        self.assertNotEqual(self.place().id, "hello")
        # checking that program doesn't initialize with *args

    def test_instance2(self):
        """Initializes with a dictionary and
        check if values initialized well"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        temp = self.place(**newIns)
        self.assertEqual(newIns["id"], temp.id)
        self.assertEqual(dt.fromisoformat(
            newIns["created_at"]), temp.created_at)
        self.assertEqual(dt.fromisoformat(
            newIns["updated_at"]), temp.updated_at)

    def test_instance3(self):
        """Checks the value type of attributes of class"""
        self.assertTrue(type(self.place().id), str)
        self.assertTrue(type(self.place().created_at), dt)
        self.assertTrue(type(self.place().updated_at), dt)

    def test_strRep(self):
        """Check the return value of __str__"""
        self.assertTrue(type(
            self.place().__str__()), str)

    def test_save1(self):
        """Checks the type value of updated_at after save function"""
        temp = self.place()
        temp.save()
        self.assertTrue(type(temp.updated_at), dt)

    def test_save2(self):
        """Checks if database exists after calling save function"""
        self.place().save()
        osList = os.listdir()
        self.assertTrue("file.json" in osList)

    def test_to_dict1(self):
        """Checks the return value of to_dict()"""
        self.assertTrue(type(self.place().to_dict()), dict)

    def test_to_dict2(self):
        """Checks if dictionary has the primary keys available"""
        data = [
            "id",
            "__class__",
            "created_at",
            "updated_at"
        ]
        for i in data:
            self.assertTrue(i in self.place().to_dict())

    def test_newValue(self):
        """Adds new Values in Place"""
        temp = self.place()
        name = "Nigeria/Kenya"
        temp.name = name
        city_id = temp.id
        temp.city_id = city_id
        user_id = temp.id
        temp.user_id = user_id
        desc = """
        Nigeria and Kenya is one good place to enjoy"""
        temp.description = desc
        num = 10
        temp.number_bathrooms = num
        temp.max_guest = num
        price = 10
        temp.price_by_night = price
        lat = 5.0
        temp.latitude = lat
        lon = 5.3
        temp.longitude = lon
        temp.number_room = num
        amIds = ["owd302", "jd292d"]
        temp.amenity_ids = amIds
        self.assertEqual(name, temp.name)
        self.assertEqual(city_id, temp.city_id)
        self.assertEqual(user_id, temp.user_id)
        self.assertEqual(desc, temp.description)
        self.assertEqual(num, temp.number_bathrooms)
        self.assertEqual(num, temp.number_room)
        self.assertEqual(num, temp.max_guest)
        self.assertEqual(price, temp.price_by_night)
        self.assertEqual(lat, temp.latitude)
        self.assertEqual(lon, temp.longitude)
        self.assertEqual(amIds, temp.amenity_ids)

        self.assertTrue("name" in temp.to_dict())
        self.assertTrue("city_id" in temp.to_dict())
        self.assertTrue("user_id" in temp.to_dict())
        self.assertTrue("description" in temp.to_dict())
        self.assertTrue("number_bathrooms" in temp.to_dict())
        self.assertTrue("number_room" in temp.to_dict())
        self.assertTrue("price_by_night" in temp.to_dict())
        self.assertTrue("latitude" in temp.to_dict())
        self.assertTrue("longitude" in temp.to_dict())
        self.assertTrue("amenity_ids" in temp.to_dict())

    def test_class_attr(self):
        """Checks the initial value of each variable
        of the place module"""
        self.assertEqual(self.place().name, "")
        self.assertEqual(self.place().city_id, "")
        self.assertEqual(self.place().user_id, "")
        self.assertEqual(self.place().description, "")
        self.assertEqual(self.place().number_bathrooms, 0)
        self.assertEqual(self.place().max_guest, 0)
        self.assertEqual(self.place().price_by_night, 0)
        self.assertEqual(self.place().latitude, 0.0)
        self.assertEqual(self.place().number_room, 0)
        self.assertEqual(self.place().longitude, 0.0)
        self.assertEqual(self.place().amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
