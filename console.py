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
        Creates a new instance of BaseModel,
        saves it to the JSON file, and prints the id
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
        Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        cls_name = args[0]
        loaded_classes = [
                obj.__class__.__name__
                for obj in storage.all().values()
                ]
        if cls_name not in loaded_classes:
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

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        and saves the change into the JSON file.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        cls_name = args[0]
        loaded_classes = [
                obj.__class__.__name__
                for obj in storage.all().values()
                ]
        if cls_name not in loaded_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = (f"{cls_name}.{obj_id}")
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        objs = storage.all()
        obj_str = [str(objs[obj] for obj in objs)]
        if not arg:
            print(obj_str)
            return
        cls_name = arg.split()[0]
        loaded_classes = [
                obj.__class__.__name__
                for obj in storage.all().values()
                ]
        if cls_name not in loaded_classes:
            print("** class doesn't exist **")
            return
        filtered_objs = [obj for obj in obj_str if cls_name in obj]
        print(filtered_objs)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        Save the change into the JSON file
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        cls_name = args[0]
        loaded_classes = [
                obj.__class__.__name__
                for obj in storage.all().values()
                ]
        if cls_name not in loaded_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = (f"{cls_name}.{obj_id}")
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
