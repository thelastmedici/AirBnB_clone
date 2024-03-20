#!/usr/bin/python3
"""import all necesarry modules"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb)'

    def emptyline(self):
        """overrides default empty line behaviour so no command is executes"""
        pass

    def do_quit(self, line):
        """quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()