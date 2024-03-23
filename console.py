#!/usr/bin/python3
"""Entry point of the AirBnB command interpreter console"""

import cmd
import re
from models.base_model import BaseModel
from models import storage
import json

class HBNBCommand(cmd.Cmd):

    """HBNBCommand class"""

    prompt = '(hbnb)'
    def default(self,line):
        """Catch commands if nothing else matches"""
        self.precmd(line)

    def _precmd(self, line):
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        class_name = match.group(1)
        args = match.group(3)
        method = match.group(2)
        match_uid_and_args = re.search(r"^\"([^\"]*)\"(?:, (.*))?$", args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            args = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attributes_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search(r"^{(.*)}$", attr_or_dict)
            if match_dict:
                self.update_dict(class_name, uid, match_dict.group(1))
                return ""
            match_attributes_and_value = re.search(r"^(\w+) (.*)$", attr_or_dict)
            attributes_and_value = (match_attributes_and_value.group(
                    1) or "") + " " + (match_attributes_and_value.group(2) or "")
        input_command = method + " " + class_name + " " + uid + " " + attributes_and_value
        self.onecmd(input_command)
        return input_command

    def update_dict(self, classname, uid, dict_str):
        """Update a dictionary of attributes"""
        s = dict_str.replace("'", '"')
        l = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = f"{classname}.{uid}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                attr = storage.attributes()[classname]
                for attributes, value in l.items():
                    if attributes in attr:
                        value = attr[attributes](value)
                    setattr(storage.all()[key], attributes, value)
                storage.all()[key].save()


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
        if  line is None or line == "":
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
        if  line is None or line == " ":
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

    def do_count(self, line):
        """" Counts the number of instances of a given class """
        arg_list = line.split(' ')
        if not  arg_list[0]:
            print("** class name missing **")
        elif arg_list[0] not in storage.classes():
            print("""** class doesn't exist **""")
        else:
            matches = [w for w in storage.all() if w.startswith(arg_list[0] + ".")]
            print(len(matches))



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
                attr = storage.attributes()[class_name]
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
