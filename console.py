#!/usr/bin/python3

import cmd, models

"""
"""
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    """
    def do_create(self, args):
        pass

    def do_show(self, args):
        pass

    def do_destroy(self):
        pass

    def do_all(self, args):
        print(models.BaseModel())
    """
    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        print()
        return True


if __name__== '__main__':
    HBNBCommand().cmdloop()
