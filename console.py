#!/usr/bin/python3
"""
Module: console.py

Import Modules:
    - cmd
    - models

ClassDefinition:
    - HBNBCommand(cmd.Cmd)
      - cmd.Cmd: is a class inherited from module "cmd"

Methods:
    - do_quit(self)
    - do_EOF(self, line)
    - emptyline(self)

    * Line as a first argument: is the expected argument after the command.
      - Ex. command -> "  line input  "
        - create -> "BaseModel" (Expected: to print BaseModel id)

Note:
    - Help command is a built-in command so there's not need to add method
      just prompt message as doc in every method
"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    Declare class instances:
       - intro: welcome message output
       - prompt: prompt message (ex: (hbnb))
    """
    # intro = "Welcome to HBNB shell interpreter! Type ? to list commands"
    prompt = '(hbnb) '
    # classes = ["BaseModel", "User", "State", "Place",
    #           "City", "Amenity", "Review"]
    classes = {"BaseModel", "User", "Place", "City", "Amenity", "Review"}
    cls = "HBNBCommand.classes"

    def do_quit(self, line):
        'Quit command to exit the program'
        return True

    def do_EOF(self, line):
        'Implement a clean way to exit: ctrl-D'
        print()
        return True

    def emptyline(self):
        'If the line is empty will not execute anything'
        return False

    def do_create(self, line):
        'Create a new instance of BaseModel'
        if not line:
            print("** class name missing **")

        elif line not in self.classes:
            print("** class doesn't exist **")

        elif line in HBNBCommand.classes:
            check = eval(line)()
            storage.new(check)
            storage.save()
            print(check.id)

    def do_destroy(self, line):
        'Deletes an instance based on the class name and id'
        if not line:
            print("** class name missing **")
            return

        if line.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return

        buffed = parse(line)

        try:
            if buffed[1]:
                string = "{}.{}".format(buffed[0], buffed[1])

                if string not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[string]
                    storage.save()

        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        'Prints a string representation of all instances'
        buffed = parse(line)
        objs = storage.all()
        objStr = []

        if len(line) == 0:
            for values in storage.all().values():
                objStr.append(values)
            print(objStr)

        elif buffed[0] in self.classes:
            for key, values in objs.items():
                if buffed[0] in key:
                    objStr[key] = objs[key]
            print(objStr)

        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        'Show a string representation of an instance'
        if not line:
            print("** class name missing **")
            return

        if line.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return

        buffed = parse(line)

        try:
            if buffed[1]:
                string = "{}.{}".format(buffed[0], buffed[1])

                if string not in storage.all().keys():
                    print("** no instance found **")
                else:
                    output = storage.all()
                    print(output[string])

        except IndexError:
            print("** instance id missing **")

    def do_update(self, line):
        'Updates an instance -> USAGE: <Class Name> <id> <attribute name>\
 "<attribute value"'
        buffed = parse(line)
        print(buffed)
        if len(buffed) == 4:
            clsKey = "{}.{}".format(buffed[0], buffed[1])
            buffed[3].strip('"')
            buffed[3].strip("'")
            setattr(storage.all()[clsKey], buffed[2], buffed[3])
        if len(buffed) == 0:
            print("** class name missing **")
            return
        if buffed[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(buffed) == 1:
            print("** instance id missing **")
            return
        checkId = "{}.{}".format(buffed[0], buffed[1])
        if checkId not in storage.all():
            print("** no instance found **")
            return
        if len(buffed) == 2:
            print("** attribute name missing **")
            return
        else:
            print("** value missing **")

    def do_count(self, line):
        'Count the number of instances of a class -> <class name>.count()'
        if line in self.classes:
            counter = 0
            for instances in storage.all().keys():
                if line in instances:
                    counter += 1
            print(counter)

        else:
            print("** class doesn't exist")

    def default(self, line):
        'Called when the syntax is not recognized unless its overriden'
        buffed = line.split(".")
        clsArg = buffed[0]
        if len(buffed) == 1:
            print("*** Unknown syntax: {}".format(buffed[0]))

        else:
            if len(buffed) == 2 and buffed[0] in self.classes:
                if buffed[1] == "count()":
                    self.do_count(clsArg)
                if buffed[1] == "all":
                    self.do_all(clsArg)


# Helper function below

def parse(line):
    'Parse a command line to get rid of whitespace'
    return tuple(line.split())

# Below is the cmd loop

if __name__ == '__main__':
    HBNBCommand().cmdloop()
