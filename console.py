#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    def emptyline(self):
        if self.lastcmd:
            self.onecmd(self.lastcmd)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
