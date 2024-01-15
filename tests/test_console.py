#!/usr/bin/python3
"""This module contains test cases for the console"""
from console import HBNBCommand
import unittest
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class TestConsole(unittest.TestCase):
    """Contains functions that are useful
    for testing the entire error message
    of the console"""
    def setUp(self):
        """Setup class for testing"""
        self.con = HBNBCommand()
        self.tem = ""
        self.msg = ""

    def test_prompt(self):
        """Checks if prompt is the same
        as directing in the project outline"""
        self.assertEqual(self.con.prompt, "(hbnb) ")

    def test_static(self):
        """Test the static method to be sure that
        strings are properly parsed"""
        temp = self.con.split_string("Boy man")
        self.assertTrue(isinstance(temp, list))
        self.assertEqual("Boy", temp[0])
        self.assertEqual("man", temp[1])

    @patch('sys.exit')
    def test_do_quit(self, mock_exit):
        """Checks if program is correctly
        when quit command is passed"""
        self.con.do_quit(None)
        mock_exit.assert_called_once_with()

    @patch('sys.exit')
    def test_do_EOF(self, mock_exit):
        """Checks if program is correctly
        when <CTRL> + <D> is pressed"""
        self.con.do_EOF(None)
        mock_exit.assert_called_once_with()

    def test_create1(self):
        """Checks the behaviour of create function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("create")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class name missing **", IOp)
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("create Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow.create()")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_create2(self):
        """Checks check function that function
        returns an id"""
        empty = [
            None,
            ""
        ]
        for i in self.con.models.keys():
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"create {i}")
                self.tem = fp.getvalue().strip()
            for j in empty:
                self.assertNotEqual(self.tem, j)

    def test_create3(self):
        """Checks check function that function
        returns an id"""
        empty = [
            None,
            ""
        ]
        for i in self.con.models.keys():
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"{i}.create()")
                self.tem = fp.getvalue().strip()
            for j in empty:
                self.assertNotEqual(self.tem, j)

    def test_show1(self):
        """Checks the behaviour of show function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("show")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class name missing **", IOp)
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("show Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)
        for i in self.con.models.keys():
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"show {i}")
                IOp = fp.getvalue().strip()
            self.assertEqual("** instance id missing **", IOp)

    def test_show2(self):
        """Checks the behaviour of show function of
        console with unusual parameters"""
        for i in self.con.models.keys():
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"show {i} o-w1e2992w1")
                IOp = fp.getvalue().strip()
            self.assertEqual("** no instance found **", IOp)
        for i in self.con.models.keys():
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"{i}.show()")
                IOp = fp.getvalue().strip()
            self.assertEqual("** no instance found **", IOp)
        for i in self.con.models.keys():
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"{i}.show(o-w1e2992w1)")
                IOp = fp.getvalue().strip()
            self.assertEqual("** no instance found **", IOp)

    def test_show3(self):
        """Checks that the print of show() is not empty
        i.e show returns a str rep of model"""
        empty = [
            None,
            ""
        ]
        for i in self.con.models.keys():
            dum = self.con.models[i]()
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"show {i} {dum.id}")
                self.msg = fp.getvalue().strip()
            for j in empty:
                self.assertNotEqual(self.msg, j)
        for i in self.con.models.keys():
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"{i}.show({dum.id})")
                self.msg = fp.getvalue().strip()
            for j in empty:
                self.assertNotEqual(self.msg, j)

    def test_destroy1(self):
        """Checks the behaviour of destroy function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("destroy")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class name missing **", IOp)
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("destroy Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow.destroy()")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_destroy2(self):
        """Checks the behaviour of destroy function of
        console with unusual parameters"""
        for i in self.con.models.keys():
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"destroy {i} o-w1e2992w1")
                IOp = fp.getvalue().strip()
            self.assertEqual("** no instance found **", IOp)
        for i in self.con.models.keys():
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"destroy {i}")
                IOp = fp.getvalue().strip()
            self.assertEqual("** instance id missing **", IOp)
        for i in self.con.models.keys():
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"{i}.destroy(o-w1e2992w1)")
                IOp = fp.getvalue().strip()
            self.assertEqual("** no instance found **", IOp)

    def test_destroy3(self):
        """Creates a destroys an instant, makes sure
        that nothing is printed in console"""
        for i in self.con.models.keys():
            dum = self.con.models[i]()
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"destroy {i} {dum.id}")
                IOp = fp.getvalue().strip()
            self.assertEqual("", IOp)

    def test_all1(self):
        """Checks the behaviour of all function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("all Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_all2(self):
        """Checks the behaviour of all function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow.all()")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_all3(self):
        """Checks behaviour in console with right params
        print in console must not be empty"""
        empty = [
            None,
            ""
        ]
        for i in self.con.models:
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"all {i}")
                IOp = fp.getvalue().strip()
                self.assertFalse(IOp in empty)
        for i in self.con.models:
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"{i}.all()")
                IOp = fp.getvalue().strip()
                self.assertFalse(IOp in empty)

    def test_update1(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("update")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class name missing **", IOp)
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("update Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_update2(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        for i in self.con.models:
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"update {i} o-w1e2992w1")
                IOp = fp.getvalue().strip()
            self.assertEqual("** attribute name missing **", IOp)
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"{i}.update(o-w1e2992w1)")
                IOp = fp.getvalue().strip()
            self.assertEqual("** attribute name missing **", IOp)
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"update {i}")
                IOp = fp.getvalue().strip()
            self.assertEqual("** instance id missing **", IOp)
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"update {i} o-w1e2992w1 first_name")
                IOp = fp.getvalue().strip()
            self.assertEqual("** value missing **", IOp)
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"update {i} o-w1e2992w1 first_name Jane")
                IOp = fp.getvalue().strip()
            self.assertEqual("** no instance found **", IOp)
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"{i}.update()")
                IOp = fp.getvalue().strip()
            self.assertEqual("** instance id missing **", IOp)
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"{i}.update(o-w1e2992w1 first_name)")
                IOp = fp.getvalue().strip()
            self.assertEqual("** value missing **", IOp)
            with patch('sys.stdout', new_callable=StringIO) as fp:
                self.con.onecmd(f"{i}.update(o-w1e2992w1 first_name Jane)")
                IOp = fp.getvalue().strip()
            self.assertEqual("** no instance found **", IOp)

    def test_update3(self):
        """Checks if attribute:value is properly created in models"""
        dumdict = {"first_name": "Jane"}
        for i in self.con.models.keys():
            dum = self.con.models[i]()
            self.con.onecmd(f"update {i} {dum.id} first_name Jane")
            self.assertEqual("Jane", dum.first_name)
            self.con.onecmd(f"{i}.update({dum.id} first_name Jane)")
            self.assertEqual("Jane", dum.first_name)
            self.con.onecmd(f"{i}.update({dum.id}, {dumdict})")
            self.assertEqual('Jane', dum.first_name)

    def test_count(self):
        """Checks the behaviour of count function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("count")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class name missing **", IOp)
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("count Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("0", IOp)
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow.count()")
            IOp = fp.getvalue().strip()
        self.assertEqual("0", IOp)

    def test_default(self):
        """Checks the behaviour of default function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("destroy.Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** Unknown syntax: Snow", IOp)
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow()")
            IOp = fp.getvalue().strip()
        self.assertEqual("** Unknown syntax: Snow()", IOp)
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow.update")
            IOp = fp.getvalue().strip()
        self.assertEqual("** Unknown syntax: Snow.update", IOp)


if __name__ == "__main__":
    unittest.main()
