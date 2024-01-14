#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class FileStoreCheck(unittest.TestCase):
    def setUp(self):
        """Initialize a fileStorage"""
        self.file = FileStorage()

    def test_all(self):
        """Checks return type of all() function"""
        self.assertTrue(type(self.file.all()) is dict)

    def test_new1(self):
        """Initial with BaseModel
        and checks existence of class in storage"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        key = f"BaseModel.{newIns['id']}"
        self.file.new(BaseModel(**newIns))
        self.assertTrue(key in self.file.all())

    def test_new2(self):
        """Initial with UserModel
        and checks existence of class in storage"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        key = f"User.{newIns['id']}"
        self.file.new(User(**newIns))
        self.assertTrue(key in self.file.all())

    def test_new3(self):
        """Initial with AmenityModel
        and checks existence of class in storage"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        key = f"Amenity.{newIns['id']}"
        self.file.new(Amenity(**newIns))
        self.assertTrue(key in self.file.all())

    def test_new4(self):
        """Initial with CityModel
        and checks existence of class in storage"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        key = f"City.{newIns['id']}"
        self.file.new(City(**newIns))
        self.assertTrue(key in self.file.all())

    def test_new5(self):
        """Initial with PlaceModel
        and checks existence of class in storage"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        key = f"Place.{newIns['id']}"
        self.file.new(Place(**newIns))
        self.assertTrue(key in self.file.all())

    def test_new6(self):
        """Initial with ReviewModel
        and checks existence of class in storage"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        key = f"Review.{newIns['id']}"
        self.file.new(Review(**newIns))
        self.assertTrue(key in self.file.all())

    def test_new7(self):
        """Initial with StateModel
        and checks existence of class in storage"""
        newIns = {
            "id": "b213d458-36b3-460b-ab99-84e82785be04",
            "created_at": "2024-01-12T08:38:06.286695",
            "updated_at": "2024-01-12T08:38:06.288367"
        }
        key = f"State.{newIns['id']}"
        self.file.new(State(**newIns))
        self.assertTrue(key in self.file.all())


if __name__ == "__main__":
    unittest.main()
