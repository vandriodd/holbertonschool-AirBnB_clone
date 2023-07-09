#!/usr/bin/python3
"""
    console module
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Class for console usage """
    valid_classes = {"BaseModel": BaseModel, "User": User,
                     "State": State, "City": City, "Amenity": Amenity,
                     "Place": Place, "Review": Review}
    prompt = "(hbnb) "

    def do_quit(self, input):
        """
        Exit program
        Usage: quit
        """
        return True

    def do_EOF(self, input):
        """
        Exit program on end-of-line (EOF)
        """
        print()
        return True

    def emptyline(self):
        """
        Ignore empty lines
        """
        pass

    def do_create(self, arg):
        """
        Creates and saves a new class instance and prints its id
        Usage: create <class name>
        """
        if arg:
            class_name = arg.split()[0]
            if class_name not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            new_ins = self.valid_classes[class_name]()
            new_ins.save()
            print(new_ins.id)
        else:
            print("** class name missing **")

    def do_show(self, input):
        """
        Prints instance details by class name and id
        Usage: show <class name> <instance id>
        """
        args = input.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            output = f"{args[0]}.{args[1]}"
            if output not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[output])

    def do_destroy(self, input):
        """
        Deletes instance by class name and id
        Usage: destroy <class name> <instance id>
        """
        args = input.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            output = f"{args[0]}.{args[1]}"
            if output not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[output]
                models.storage.save()

    def do_all(self, input):
        """
        Prints string representations of instances by class or all
        Usage: all <class name>
        """
        all_inst = models.storage.all()
        if input:
            if input not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            else:
                result = []
                for k in all_inst:
                    if str(k).startswith(input):
                        result.append(str(all_inst[k]))
                print(result)
        else:
            for k in all_inst.keys():
                print(str(all_inst[k]))

    def do_update(self, input):
        """
        Updates instance attribute by class and id
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = input.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            class_name = args[0]
            obj_id = args[1]
            attr_name = args[2]
            attr_value = args[3]
            a_ty = type(getattr(self.valid_classes[class_name], attr_name, ""))
            key = f"{class_name}.{obj_id}"
            if key in models.storage.all():
                setattr(models.storage.all()[key], attr_name, a_ty(attr_value))
                models.storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
