#!/usr/bin/python3
"""
This module defines the HBNBCommand
"""

import json
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handle EOF signal to exit the program."""
        return True

    def emptyline(self):
        """Handle empty line."""
        pass

    def do_create(self, args):
        """Create a new instance of BaseModel, save it to the JSON file and print the id."""
        if len(args) == 0:
            print("** class name missing **")
        elif args not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj = storage.create(args)
            print(obj.id)

    def do_show(self, args):
        """Print the string representation of an instance based on the class name and id."""
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, args):
        """Delete an instance based on the class name and id (save the change into the JSON file)."""
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, args):
        """Print all string representation of all instances based or not on the class name."""
        if len(args) == 0:
            for obj in storage.all().values():
                print(obj)
        else:
            if args not in storage.classes():
                print("** class doesn't exist **")
            else:
                for obj in storage.all().values():
                    if type(obj).__name__ == args:
                        print(obj)

    def do_update(self, args):
        """Update an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif len(arg_list) == 2:
            print("** attribute name missing **")
        elif len(arg_list) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                setattr(obj, arg
