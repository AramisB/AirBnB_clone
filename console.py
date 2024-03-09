#!/usr/bin/python3
"""
This module defines the HBNBCommand
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Represents the HBNBCommand of the HBNB project
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """Handles empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of file command"""
        print (" ")
        return True

