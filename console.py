#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.errors import *
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = storage.models


class HBNBCommand(cmd.Cmd):
    """the console for the airbnb clone project
    all interactions are done through this class"""

    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Override empty line to do nothing"""
        return

    def do_create(self, args):
        """create new instance of BaseModel, saves it
        (to the JSON file)
        throws error if model name doesnot exist or missing"""

        args, n = parse(args)

        if not n:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif n == 1:
            tmp = eval(args[0])()
            print(tmp.id)
            tmp.save()
        else:
            print("** Too many argument for create **")
            pass

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""

        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")

        elif n == 2:
            try:
                instance = storage.find_by_id(*args)
                print(instance)
            except ModelNotFoundError:
                print("** class doesn't exist **")

            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for show **")
            pass

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""

        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                storage.del_by_id(args)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for destroy **")
            pass

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""

        args, n = parse(arg)
        if n < 2:
            try:
                print(storage.find_all(*args))
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            print("** Too many argument for all **")
            pass

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        args, n = parse(arg)
        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            print("** attribute name missing **")
        elif n == 3:
            print("** value missing **")
        else:
            try:
                storage.update_1(*args[0:4])
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
                
    def do_models(self, arg):
        """print all registered models"""
        print(*classes)

    def handle_cls_m(self, arg):
        """handles class methods"""

        prints = ("all(", "show(", "count(", "create(")
        try:
            value = eval(arg)
            for i in prints:
                if i in arg:
                    print(value)
                    break
            return
        except AttributeError:
            print("** invalid method **")
        except InstanceNotFoundError:
            print("** no instance found **")
        except TypeError as t:
            field = t.args[0].split()[-1].replace("_", " ")
            field = field.strip("'")
            print(f"** {field} missing **")
        except Exception as e:
            print("** invalid syntax **")
            pass

    def default(self, arg):
        """Override default method to handle class methods"""
        if '.' in arg and arg[-1] == ')':
            if arg.split('.')[0] not in classes:
                print("** class doesn't exist **")
                return
            return self.handle_class_methods(arg)
        return Cmd.default(self, arg)

    def emptyline(self):
        """Override empty line to do nothing"""
        return


def parse(line: str):
    """splits lines to words using spaces"""
    args = shlex.split(line)
    return args, len(args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
