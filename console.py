#!/usr/bin/python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    intro = "AirBnB project, Type ? or help to list commands"
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("Bye 👋")
        sys.exit()

    def do_EOF(self, arg):
        """This function will close the program after to indicate EOF"""
        print("Bye 👋")
        sys.exit()

    def do_help(self, arg):
        """Get help on a specific command."""
        cmd.Cmd.do_help(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
