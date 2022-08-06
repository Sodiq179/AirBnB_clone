#!/usr/bin/python3
'''File Storage system'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''serializes and deserialzes json files'''

    __file_path = 'file.json'
    __objects = {}
    dict = {"BaseModel": BaseModel, "Review": Review, "Place": Place,
            "State": State, "Amenity": Amenity, "City": City, "User": User}

    def all(self):
        '''Returns dictionary of the object instance'''
        return self.__objects

    def new(self, obj):
        '''Adds new object, obj, to the dictionary'''
        if obj:
            key = f'{obj.__class__.__name__}.{obj.id}'
            self.__objects[key] = obj

    def save(self):
        '''Save obj dictionaries to json file'''
        dict = {}

        for key, obj in self.__objects.items():
            dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(dict, file)

    def reload(self):
        '''Converts obj dicts back to instances if json file exists'''
        try:
            with open(FileStorage.__file_path, 'r') as file:
                new_obj = json.load(file)
            for key, val in new_obj.items():
                obj = self.dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass