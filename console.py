#!/usr/bin/python3
import cmd
import sys
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            arg = BaseModel()
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
        keydict = [str(keys[i]) for i in keys.keys()]
        print(keydict)

        



if __name__ == '__main__':
    HBNBCommand().cmdloop()
