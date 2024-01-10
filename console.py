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

    def do_emptyline(self, arg):
        return
    
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
        elif arg.startswith("BaseModel"):
            try:
                args = self.split_string(arg, " ")
                obj = f"{args[0]}.{args[1]}"
                keys = storage.all()
                for i in keys.keys():
                    if i == obj:
                        print(keys[i])
                        return
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
        
    def do_destroy(self, arg):
        if arg == "":
            print("** class name missing **")
        elif arg.startswith("BaseModel"):
            try:
                args = self.split_string(arg, " ")
                obj = f"{args[0]}.{args[1]}"
                keys = storage.all()
                del keys[obj]
                storage.save()
            except IndexError:
                print("** instance id missing **")
            except KeyError:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        keys = storage.all()
        keydict = []
        if arg == "":
            keydict = [str(keys[i]) for i in keys.keys()]
        elif arg == "BaseModel":
            for i in keys.keys():
                if i.startswith("BaseModel"):
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
            if args[0] != "BaseModel":
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
