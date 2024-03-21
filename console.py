#!/usr/bin/python3
"""import all necesarry modules"""

import cmd
from models.engine import storage

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
        if line != "" and line is not None:
             print("** class name missing **")
        elif line not in storage.classes():
                print("** class doesn't exist **")
        else:
             i = storage.classes()[line]()
             i.save()
             print(i.id)



if __name__ == '__main__':

    HBNBCommand().cmdloop()
