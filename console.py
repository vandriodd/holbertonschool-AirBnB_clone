#!/usr/bin/python3
"""
    console module
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ Class for console usage """
    prompt = "(hbnb) "

    def do_quit(self, input):
        """ Exits the console """
        print()
        return True

    def do_EOF(self, input):
        """ Exits the console """
        print()
        return True

    def emptyline(self):
        """ Doesn't do anything when an empty line is passed """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
