#!/usr/bin/python3
"""This Module is the command-line interpreter of the Class

All functions and properties of each class can be
executed via the command line with basic command line interface

Type <help> <command>
"""
import cmd
import sys
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Represents the CLI of the program

    Methods:
        do_quit: Quits the program
        do_EOF: Quits program if command is <CTRL + D>
        do_help: Contains the help information of commands
        do_create: creates new instance bsed on class
        do_show: shows the detail of file.json based on class and id
        do_destroy: destroys an instance based on class and id
        do_all: prints all instances in file.json or only of a class
        do_update: updates a class with name:value based on class and id
        do_count: counts the number of instances present in database
        default: to parse commands that are <classname>.<command>
        emptyline: prints/returns nothing if line is empty
    """
    prompt = "(hbnb) "
    models = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    @staticmethod
    def split_string(input=None, deli=" "):
        """Function split a given string based on char

        Args:
            input (str): The input string from user
            deli (str): The delimiter for breaking strings

        Return:
            a list of broken string
        """
        if input is not None:
            return input.split(deli)

    def do_quit(self, arg):
        """Quit command to exit the program

        Usage: quit
        """
        sys.exit()

    def do_EOF(self, arg):
        """This function will close the program after to indicate EOF

        Usage: <CTRL> + <D>
        """
        sys.exit()

    def do_help(self, arg):
        """Get help on a specific command

        Usage: help 'or' help <command>
        """
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """Creates a new instance based on class name
        and saves it to file.json

        Usage: create <classname> 'or'
        <class name>.create()

        Errors:
            if class name is missing
            if class name doesn't exist
        """
        argl = self.split_string(arg)
        if argl[0] == "":
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            arg = HBNBCommand.models[argl[0]]()
            print(arg.id)
            arg.save()

    def do_show(self, arg):
        """Prints all the instance details
        based on the classname and classId

        Usage: show <class.name> <class.id> 'or'
        <class name>.show(<id>)

        Errors:
            if classname is missing
            if classname doesn't exist
            if class id is not found
            if class id is missing
        """
        if arg == "":
            print("** class name missing **")
            return
        try:
            args = self.split_string(arg, " ")
            if args[0] not in HBNBCommand.models:
                print("** class doesn't exist **")
                return
            obj = f"{args[0]}.{args[1]}"
            keys = storage.all()
            for i in keys.keys():
                if i == obj:
                    print(keys[i])
                    return
            print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Function destroys a class instance
        based on classname and classId

        Usage: destroy <class.name> <class.id> 'or'
        <class name>.destroy(<id>)

        Errors:
            if classname is missing
            if classname doesn't exist
            if class id is not found
            if class id is missing
        """
        if arg == "":
            print("** class name missing **")
            return
        try:
            args = self.split_string(arg, " ")
            if args[0] not in HBNBCommand.models:
                print("** class doesn't exist **")
                return
            obj = f"{args[0]}.{args[1]}"
            keys = storage.all()
            del keys[obj]
            storage.save()
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Displays all the instances/instances of a class

        Usage: all 'or' all <class name> 'or'
        <class name>.all()

        Errors:
            if class name doesn't exist
        """
        keys = storage.all()
        keydict = []
        argl = self.split_string(arg)
        if argl[0] == "":
            keydict = [str(keys[i]) for i in keys.keys()]
        elif argl[0] in HBNBCommand.models:
            for i in keys.keys():
                if i.startswith(argl[0]):
                    keydict.append(str(keys[i]))
        else:
            print("** class doesn't exist **")
            return
        print(keydict)

    def do_update(self, arg):
        """Function updates an instance
        based on classname, id and name:value

        Usage: update <class name> <id>
        <attribute name> <attribute value...> 'or'
        <class name>.update(<id>, <attribute name>, <attribute value>)

        Errors:
            if classname is missing
            if classname doesn't exist
            if class id is not found
            if class id is missing
            if attribute name is missing
            if attribute value is missing
        """
        try:
            if arg == "":
                raise NameError
            args = self.split_string(arg)
            if args[0] not in HBNBCommand.models:
                print("** class doesn't exist **")
                return
            elif len(args) == 1 or args[1] == "":
                print("** instance id missing **")
                return
            elif len(args) == 2:
                print("** attribute name missing **")
                return
            name = f"{args[0]}.{args[1]}"
            odict = {}
            for i in range(2, len(args), 2):
                key = args[i]
                key = key.replace("{", "").replace(":", "")
                key = key.replace("}", "").replace('"', "")
                value = args[i + 1]
                value = value.replace("{", "").replace(":", "")
                value = value.replace("}", "").replace('"', "")
                odict[key] = value
            keys = storage.all()
            if name in keys:
                obj = keys[name]
                for i, j in odict.items():
                    setattr(obj, i, j)
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print('** class name missing **')
        except IndexError:
            print("** value missing **")

    def do_count(self, arg):
        """Counts the number of instances present in database

        Usage: <class name>.count()
        """
        if arg == "":
            print("** class name missing **")
            return
        argl = self.split_string(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def emptyline(self):
        """Do nothing to screen"""
        return

    def default(self, arg):
        """Parse commands that are <classname>.<command>
        e.g User.create()
        and checks if command is True"""
        coms = {
            "create": self.do_create,
            "all": self.do_all,
            "count": self.do_count,
            "update": self.do_update,
            "destroy": self.do_destroy,
            "show": self.do_show
        }
        # model: model name
        # act: the command to execute
        # det: other parameters in "()"
        # shorten because of pycodestyle
        args = re.match(r"(?P<model>\w+)\.(?P<act>\w+)\((?P<det>.*?)\)", arg)
        if args:
            model = args.group("model")
            act = args.group("act")
            det = args.group("det")
            det = det.replace(",", "")
            coms[act](f"{model} {det}")
        else:
            print(f"** Unknown syntax: {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
