#!/usr/bin/python3

"""
The console program is defined here

"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpretrer class"""

    prompt = "(hbnb) "

    def do_create(self, class_name):
        """
        Create an instance of the given class

        Args:
            class_name (str): name of class to create an instance of
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

        Usage: [class name] [instance id]

               Enter class name and id of the instance to show
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
            memory = FileStorage()  # create an instance of FileStorage
            mem_dict = memory.all()  # get __objects attribute of FileStorage

            # Search for the instance by the key <class_name>.<obj_id>
            # in __objects dictionary of stored objects
            found_dict = {key_id: obj for key_id, obj in mem_dict.items()
                          if key_id == f"{class_name}.{obj_id}"}

            found_obj = [obj for obj in found_dict.values()]  # extract object

            print("** no instance found **") if found_dict == {} else print(
                found_obj[0])  # print obj if obj exist else print the err msg

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
