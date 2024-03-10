#!/usr/bin/python3
"""
A module that defines HBNBCommand CLI
"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    A class HBNBCommand for the HBNB project CLI
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when EOF (Ctrl + D) is encountered
        """
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file, and prints the id
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split()
        cls_name = arg[0]
        if cls_name not in storage.__classes():
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = arg[1]
        key = (f"{cls_name}.{obj_id}")
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
