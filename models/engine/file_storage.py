#!/usr/bin/python3
"""This module defines the FileStorage class"""
import json
import datetime
import os

class FileStorage():
    """A class   that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """public instance method that
        returns the dictionary __objects"""
        return self.__objects

    def new(self,obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_name = obj.__class__.__name__
        obj_id = obj.id
        key = "{}.{}".format(obj_name, obj_id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        object_dict = {}
        for key in self.__objects.keys():
            if type(self.__objects[key]) != dict:
                object_dict[key] = self.__objects[key].to_dict()
        file_name = self.__file_path
        with open(file_name, "w", encoding='utf-8') as jsonfile:
            jsonfile.write(json.dumps(object_dict))


    def reload(self):
        """Reload the stored objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding='utf-8') as jsonfile:
                object_dict = json.load(jsonfile.read())
            final_dict = {}

            for id, dictionary in object_dict.items():
                class_name = dictionary["__class__"]
                final_dict[id] = self.classes()[class_name](**dictionary)
            FileStorage.__objects = final_dict
