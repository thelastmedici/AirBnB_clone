#!/usr/bin/python3
"""import all necesarry modules"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class HBNBCommand(cmd.Cmd):

    """HBNBCommand class"""

    prompt = '(hbnb)'

    def emptyline(self):
        """opip install pycodestyleverrides default empty line behaviour so no command is executes"""
        pass

    def do_quit(self, line):
        """quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, line):
        """Creates an instance saves it to JSON file and prints the id"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """ Prints the string representation of an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            arg_list = line.split(' ')
            if arg_list[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            else:
                dict_key = f"{arg_list[0]}.{arg_list[1]}"
                if dict_key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[dict_key])

    def  do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == "" or line is None:
            print("""** class name missing **""")
        else:
            arg_list = line.split(' ')
            if arg_list[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            else:
                dict_key = f"{arg_list[0]}.{arg_list[1]}"
                if dict_key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[dict_key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        if line != "":
            arg_list = line.split(' ')
            if arg_list[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj_rep = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == arg_list[0]]

                print(obj_rep)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
            return
        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        class_name = match.group(1)
        uid = match.group(2)
        attr = match.group(3)
        val = match.group(4)
        if not match:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = f"{class_name}.{uid}"
            if key not in storage.all():
                print("""** no instance found **""")
            elif not attr:
                print("** attribute name missing **")
            elif not val:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', val):
                    if "." not in val:
                        cast = int
                    else:
                        cast = float
                else:
                    val = val.replace('"', '')
                attr = storage.attr()[class_name]
                if attr in attr:
                    val = attr[attr](val)
                elif cast:
                    try:
                        val = cast(val)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attr, val)
                storage.all()[key].save()

if __name__ == '__main__':


    HBNBCommand().cmdloop()
