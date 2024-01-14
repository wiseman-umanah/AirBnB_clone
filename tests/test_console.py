#!/usr/bin/python3
"""This module contains test cases for the console"""
from console import HBNBCommand
import unittest
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Contains functions that are useful
    for testing the entire error message
    of the console"""
    def setUp(self):
        """Setup class for testing"""
        self.con = HBNBCommand()

    def test_prompt(self):
        """Checks if prompt is the same
        as directing in the project outline"""
        self.assertEqual(self.con.prompt, "(hbnb) ")

    def test_models(self):
        """Checks if models are available in
        console dictionary containing models"""
        classes = [
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "Review",
            "State"
        ]
        for i in classes:
            self.assertTrue(i in self.con.models)

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

    def test_create1(self):
        """Checks the behaviour of create function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("create")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class name missing **", IOp)

    def test_create2(self):
        """Checks the behaviour of create function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("create Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_create3(self):
        """Checks the behaviour of create function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow.create()")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_show1(self):
        """Checks the behaviour of show function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("show")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class name missing **", IOp)

    def test_show2(self):
        """Checks the behaviour of show function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("show Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_show3(self):
        """Checks the behaviour of show function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("show BaseModel o-w1e2992w1")
            IOp = fp.getvalue().strip()
        self.assertEqual("** no instance found **", IOp)

    def test_show4(self):
        """Checks the behaviour of show function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("show User")
            IOp = fp.getvalue().strip()
        self.assertEqual("** instance id missing **", IOp)

    def test_show5(self):
        """Checks the behaviour of show function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("BaseModel.show()")
            IOp = fp.getvalue().strip()
        self.assertEqual("** no instance found **", IOp)

    def test_show6(self):
        """Checks the behaviour of show function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("BaseModel.show(o-w1e2992w1)")
            IOp = fp.getvalue().strip()
        self.assertEqual("** no instance found **", IOp)

    def test_destroy1(self):
        """Checks the behaviour of destroy function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("destroy")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class name missing **", IOp)

    def test_destroy2(self):
        """Checks the behaviour of destroy function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("destroy Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_destroy3(self):
        """Checks the behaviour of destroy function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("destroy BaseModel o-w1e2992w1")
            IOp = fp.getvalue().strip()
        self.assertEqual("** no instance found **", IOp)

    def test_destroy4(self):
        """Checks the behaviour of destroy function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("destroy User")
            IOp = fp.getvalue().strip()
        self.assertEqual("** instance id missing **", IOp)

    def test_destroy5(self):
        """Checks the behaviour of destroy function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow.destroy()")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_destroy6(self):
        """Checks the behaviour of destroy function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("BaseModel.destroy(o-w1e2992w1)")
            IOp = fp.getvalue().strip()
        self.assertEqual("** no instance found **", IOp)

    def test_destroy7(self):
        """Checks the behaviour of destroy function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("User.destroy()")
            IOp = fp.getvalue().strip()
        self.assertEqual("** no instance found **", IOp)

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

    def test_update1(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("update")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class name missing **", IOp)

    def test_update2(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("update Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_update3(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("update BaseModel o-w1e2992w1")
            IOp = fp.getvalue().strip()
        self.assertEqual("** attribute name missing **", IOp)

    def test_update4(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("update User")
            IOp = fp.getvalue().strip()
        self.assertEqual("** instance id missing **", IOp)

    def test_update5(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("update BaseModel o-w1e2992w1 first_name")
            IOp = fp.getvalue().strip()
        self.assertEqual("** value missing **", IOp)

    def test_update6(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("update BaseModel o-w1e2992w1 first_name Jane")
            IOp = fp.getvalue().strip()
        self.assertEqual("** no instance found **", IOp)

    def test_update7(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow.update()")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_update8(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("BaseModel.update(o-w1e2992w1)")
            IOp = fp.getvalue().strip()
        self.assertEqual("** attribute name missing **", IOp)

    def test_update9(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("User.update()")
            IOp = fp.getvalue().strip()
        self.assertEqual("** instance id missing **", IOp)

    def test_update10(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("BaseModel.update(o-w1e2992w1 first_name)")
            IOp = fp.getvalue().strip()
        self.assertEqual("** value missing **", IOp)

    def test_update11(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("BaseModel.update(o-w1e2992w1 first_name Jane)")
            IOp = fp.getvalue().strip()
        self.assertEqual("** no instance found **", IOp)

    def test_update12(self):
        """Checks the behaviour of update function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd(
                "BaseModel.update(o-w1e2992w1,{first_name: Jane})"
                )
            IOp = fp.getvalue().strip()
        self.assertEqual("** no instance found **", IOp)

    def test_count1(self):
        """Checks the behaviour of count function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("count")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class name missing **", IOp)

    def test_count2(self):
        """Checks the behaviour of count function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("count Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("0", IOp)

    def test_count2(self):
        """Checks the behaviour of count function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow.count()")
            IOp = fp.getvalue().strip()
        self.assertEqual("0", IOp)

    def test_default1(self):
        """Checks the behaviour of default function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("destroy.Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** class doesn't exist **", IOp)

    def test_default2(self):
        """Checks the behaviour of default function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow")
            IOp = fp.getvalue().strip()
        self.assertEqual("** Unknown syntax: Snow", IOp)

    def test_default2(self):
        """Checks the behaviour of default function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow()")
            IOp = fp.getvalue().strip()
        self.assertEqual("** Unknown syntax: Snow()", IOp)

    def test_default2(self):
        """Checks the behaviour of default function of
        console with unusual parameters"""
        with patch('sys.stdout', new_callable=StringIO) as fp:
            self.con.onecmd("Snow.update")
            IOp = fp.getvalue().strip()
        self.assertEqual("** Unknown syntax: Snow.update", IOp)


if __name__ == "__main__":
    unittest.main()
