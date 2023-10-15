#!/usr/bin/python3

"""
The console program is defined here

"""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Command interpretrer class"""

    prompt = "(hbnb) "

    @staticmethod
    def mould(args, action):
        """
        This is a template for `show()` and `destroy()`. Since they
        have the same structure, all processes will be carried out
        in this method and the final execution will be defined by
        the `action` argument.

        Args:
            args (str): String of arguments seperated by space
            action (str): flag to decide whether to print or delete
        """

        splited = args.split(" ")

        if splited[0] == "":
            print("** class name missing **")
        elif splited[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(splited) == 1:
            print("** instance id missing **")
        else:

            class_name, obj_id = splited[0], splited[1]
            mem_dict = storage.all()  # get __objects attribute of FileStorage

            # Search for the instance by the key: <class_name>.<obj_id>
            # in __objects dictionary of stored objects
            found_dict = {key_id: obj for key_id, obj in mem_dict.items()
                          if key_id == f"{class_name}.{obj_id}"}

            found_obj = [obj for obj in found_dict.values()]  # extract object
            found_key = [obj for obj in found_dict.keys()]  # extract key

            if action == "print":
                print("** no instance found**") if found_dict == {} else print(
                    found_obj[0])  # print obj if obj exist else print err msg
            else:
                if found_dict == {}:
                    print("** no instance found **")
                else:
                    del mem_dict[found_key[0]]

    @staticmethod
    def convector(txt):
        """
        Converts the given str into int, float or string

        Args:
           txt (str): string to be converted

        Return:
            The appropraite type
        """
        if txt[0] == '\"' and txt[-1] == '\"':
            txt = txt[1:-1]

        if txt.isdigit():
            return int(txt)
        else:
            try:
                txt = float(txt)
                return txt
            except ValueError:
                return txt

    def do_create(self, class_name):
        """
        Create an instance of the given class

        Args:
            class_name (str): name of class to create an instance of

        Usage: create <class name>

               Enter class name to be created
               Upon success, the id of the insatnce will be printed out
        """
        if class_name == "BaseModel":
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)
        elif class_name == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Print out an instance given by it's class name and id

        Args:
            args (str): String of arguments seperated by space

        Usage: show <class name> <instance id>

               Enter class name and id of the instance to show
        """
        HBNBCommand.mould(args, "print")

    def do_destroy(self, arg):
        """
        Remove instances from storage

        Args:
            args (str): String of arguments seperated by space

        Usage: destroy <class name> <instance id>

               Enter class name and id of the instance to remove
        """

        HBNBCommand.mould(arg, "delete")

    def do_all(self, class_name):
        """
        Print a list of all string representation of all the objects in:
        i. The class if a class name is given
        ii. All classes currently within storage if no class name is given

        Args:
            class_name (str): class whose objects is to be printed

        Usage: all [class name]

               Enter the class name to print
        """

        # create an instance of FileStorage
        mem_dict = storage.all()  # get __objects attribute of FileStorage

        if class_name != "":
            # in __objects dictionary of stored objects
            found_dict = {key_id: obj for key_id, obj in mem_dict.items()
                          if key_id.startswith(f"{class_name}")}

            if found_dict == {}:
                print("** class doesn't exist **")
            else:
                found_obj = [obj for obj in found_dict.values()]  # extract obj
                found_obj = [obj.__str__() for obj in found_obj]
                print(found_obj)
        else:
            all_obj = [obj for obj in mem_dict.values()]  # extract object
            all_obj = [obj.__str__() for obj in all_obj]  # convert to str rep
            print(all_obj)

    def do_update(self, args):
        """
        Create or Upadate an attribute of an instance by the given
        class name and id.

        Args:
            args (str): String of arguments seperated by space

        Usage: update <class name> <id> <attribute name> "<attribute value>"

               The attribute of the instance <class name>.<id> will be created
               or updated with the given <attribute name>: "<attribute value>"

        """

        splited = args.split(" ")

        if len(splited) >= 2:
            class_name, obj_id = splited[0], splited[1]
            # create an instance of FileStorage
            mem_dict = storage.all()  # get __objects attribute of FileStorage

            found_dict = {key_id: obj for key_id, obj in mem_dict.items()
                          if key_id == f"{class_name}.{obj_id}"}
        else:
            found_dict = {}

        if splited[0] == "":
            print("** class name missing **")
        elif splited[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(splited) == 1:
            print("** instance id missing **")
        elif found_dict == {}:
            print("** no instance found**")
        elif len(splited) == 2:
            print("** attribute name missing **")
        elif len(splited) == 3:
            print("** value missing **")
        else:
            attr_name, attr_val = splited[2], splited[3]
            found_obj = [obj for obj in found_dict.values()]  # extract object
            obj = found_obj[0]

            # convert the attribute value to it's appropraite type
            attr_val = HBNBCommand.convector(attr_val)

            obj.__dict__[attr_name] = attr_val
            obj = obj.to_dict()
            obj = BaseModel(**obj)
            obj.save()

    def do_quit(self, line):
        """Quit command exits program"""
        return True

    def do_EOF(self, line):
        """Handels end-of-file by exiting the program"""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
