#!/usr/bin/python3
"""
Command interpreter for the AirBnB clone project.
It allows for creating, retrieving, updating, and destroying objects.
"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from colorama import Fore, init

init(autoreset=True)


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_create(self, arg):
        """Creates a new instance of a class and saves it to the file."""
        if arg in self.classes:
            obj = self.classes[arg]()
            obj.save()
            print(obj.id)
        else:
            print(Fore.RED + "** class doesn't exist **")

    def do_show(self, arg):
        """Shows the string representation of an instance based on class name and ID."""
        args = arg.split()
        if len(args) < 1:
            print(Fore.RED + "** class name missing **")
            return
        elif args[0] not in self.classes:
            print(Fore.RED + "** class doesn't exist **")
            return

        if len(args) < 2:
            print(Fore.RED + "** instance id missing **")
            return

        obj = storage.get(self.classes[args[0]], args[1])
        if obj is None:
            print(Fore.RED + "** no instance found **")
        else:
            print(Fore.GREEN + str(obj))

    def do_destroy(self, arg):
        """Destroys an instance based on class name and ID."""
        args = arg.split()
        if len(args) < 1:
            print(Fore.RED + "** class name missing **")
            return
        elif args[0] not in self.classes:
            print(Fore.RED + "** class doesn't exist **")
            return

        if len(args) < 2:
            print(Fore.RED + "** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            print(Fore.GREEN + "** instance deleted **")
        else:
            print(Fore.RED + "** no instance found **")
    


    def do_all(self, arg):
        """Shows all instances of a given class."""
        args = arg.split()
        if len(args) < 1:
            print(Fore.RED + "** class name missing **")
            return

        if args[0] not in self.classes:
            print(Fore.RED + "** class doesn't exist **")
            return

        objs = storage.all(self.classes[args[0]])  # Fetch all objects of the given class
        if objs:
            for obj in objs.values():
                print(Fore.GREEN + str(obj))
        else:
            print(Fore.RED + "** no instances found **")




    def do_update(self, arg):
        """Updates an instance based on class name, id, and attribute."""
        args = arg.split()
        if len(args) < 1:
            print(Fore.RED + "** class name missing **")
        elif args[0] not in self.classes:
            print(Fore.RED + "** class doesn't exist **")
        elif len(args) < 2:
            print(Fore.RED + "** instance id missing **")
        elif len(args) < 3:
            print(Fore.RED + "** attribute name missing **")
        elif len(args) < 4:
            print(Fore.RED + "** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()
                print(Fore.GREEN + "** instance updated **")
            else:
                print(Fore.RED + "** no instance found **")

    def do_count(self, arg):
        """Counts the number of instances of a given class."""
        args = arg.split()
        if len(args) < 1:
            print(Fore.RED + "** class name missing **")
            return

        if args[0] not in self.classes:
            print(Fore.RED + "** class doesn't exist **")
            return

        count = storage.count(self.classes[args[0]])  # Counts the instances of the class
        print(Fore.GREEN + f"Number of {args[0]} instances: {count}")

    def do_get(self, arg):
        """Gets an object by class and ID."""
        args = arg.split()
        if len(args) < 1:
            print(Fore.RED + "** class name missing **")
        elif args[0] not in self.classes:
            print(Fore.RED + "** class doesn't exist **")
        elif len(args) < 2:
            print(Fore.RED + "** instance id missing **")
        else:
            obj = storage.get(self.classes[args[0]], args[1])
            if obj:
                print(Fore.GREEN + str(obj))
            else:
                print(Fore.RED + "** no instance found **")

    def default(self, line):
        """Handles commands not in the standard set."""
        match = re.match(r"(\w+)\.(\w+)\((.*?)\)", line)
        if match:
            cls_name, command, args = match.groups()
            if cls_name in self.classes:
                method = getattr(self, f"do_{command}", None)
                if method:
                    args = args.replace('"', '').replace(",", " ")
                    method(f"{cls_name} {args}")
                    return
        print(Fore.RED + "** command not recognized **")

    def do_quit(self, arg):
        """Exits the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Handles EOF and exits the program."""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
