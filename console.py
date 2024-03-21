#!/usr/bin/python3
"""import all necesarry modules"""

import cmd
from models import storage

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
        '''Function to create a new instance of a class'''
        if line == "" or line is not None:
             print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
             i = storage.classes()[line]()
             i.save()
             print(i.id)

    def do_show(self, line):
         '''Function to print the string representation of an instance based on the class name and id'''
         if line == "" or line is not None:
             print("** class name missing **")
         else:
              arg_list = line.split(' ')
              if arg_list[0] not in storage.classes():
                  print("** class doesn't exist **")
              elif len(arg_list) < 2:
                    print("** instance id missing **")
              else:
                    key = arg_list[0] + "." + arg_list[1]
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")


if __name__ == '__main__':

    HBNBCommand().cmdloop()
