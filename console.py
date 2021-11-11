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

Note:
    - Help command is a built-in command so there's not need to add method
      just prompt message as doc in every method
"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Declare class instances:
       - intro: welcome message output
       - prompt: prompt message (ex: (hbnb))
    """
    intro = "Welcome to HBNB shell interpreter! Type ? to list commands"
    prompt = '(hbnb) '

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

# Below is the cmd loop

if __name__ == '__main__':
    HBNBCommand().cmdloop()
