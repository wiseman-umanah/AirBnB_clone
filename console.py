#!/usr/bin/python3
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
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
    def split_string(input=None, char=" "):
        if input is not None:
            return input.split(char)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """This function will close the program after to indicate EOF"""
        sys.exit()

    def do_help(self, arg):
        """Get help on a specific command."""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        if arg == "":
            print("** class name missing **")
        elif arg not in HBNBCommand.models:
            print("** class doesn't exist **")
        else:
            arg = HBNBCommand.models[arg]()
            print(arg.id)
            arg.save()

    def do_show(self, arg):
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
        keys = storage.all()
        keydict = []
        if arg == "":
            keydict = [str(keys[i]) for i in keys.keys()]
        elif arg in HBNBCommand.models:
            for i in keys.keys():
                if i.startswith(arg):
                    keydict.append(str(keys[i]))
        else:
            print("** class doesn't exist **")
            return
        print(keydict)

    def do_update(self, arg):
        try:
            if arg == "":
                raise NameError
            args = self.split_string(arg)
            if args[0] not in HBNBCommand.models:
                print("** class doesn't exist **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            elif len(args) == 2:
                print("** attribute name missing **")
                return
            name = f"{args[0]}.{args[1]}"
            odict = {args[i]: args[i + 1] for i in range(2, len(args), 2)}
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

    def emptyline(self):
        return

    # def default(self, arg):
    #     print(len(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
