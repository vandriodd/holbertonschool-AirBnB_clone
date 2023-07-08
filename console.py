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
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ Class for console usage """
    valid_classes = {"BaseModel": BaseModel, "User": User,
                     "State": State, "City": City, "Amenity": Amenity,
                     "Place": Place, "Review": Review}
    prompt = "(hbnb) "

    def do_quit(self, input):
        """ Exits the console """
        return True

    def do_EOF(self, input):
        """ Exits the console """
        print()
        return True

    def emptyline(self):
        """ Doesn't do anything when an empty line is passed """
        pass

    def do_create(self, class_name):
        """ Creates a new instance of a class, saves it to
        JSON file and prints the id """
        class_name = class_name.split()[0]
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        else:
            new_ins = self.valid_classes[class_name]()
            new_ins.save()
            print(new_ins.id)

    def do_show(self, input):
        """ Prints the string representation of an
        instance based on the class name """
        args = input.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            output = f"{args[0]}.{args[1]}"
            if output not in models.storage.all():
                print("** no instance found **")
                return
            else:
                print(models.storage.all()[output])

    def do_destroy(self, input):
        """ Deletes an instance based on the class name and id """
        args = input.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            output = f"{args[0]}.{args[1]}"
            if output not in models.storage.all():
                print("** no instance found **")
                return
            else:
                del models.storage.all()[output]
                models.storage.save()

    def do_all(self, input):
        """ Prints all string representation of all instances, based
        or not on the class name """
        all_inst = models.storage.all()
        if input:
            if input not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            else:
                result = []
                for k in all_inst.keys():
                    if str(k).startswith(input):
                        result.append(str(all_inst[k]))
                print(result)
        else:
            for k in all_inst.keys():
                print(str(all_inst[k]))

    def do_update(self, input):
        """ Updates an instance adding/setting an attribute """
        args = input.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
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
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
