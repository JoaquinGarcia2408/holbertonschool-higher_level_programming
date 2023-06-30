#!/usr/bin/python3
"Rewriting of the Base class"
import json
import os.path


class Base():
    "Base Class"
    __nb_objects = 0

    def __init__(self, id=None):
        "Instantiation"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        "Returns the JSON repr of list_dictionaries"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            # devuelve la serializacion en JSON de list_dictionaries
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        "Writes the JSON str repr of list_objs to a file"
        filename = f"{cls.__name__}.json"
        dicted = []
        if list_objs is None:
            return []
        else:
            for i in list_objs:
                dicted.append(i.to_dictionary())
            with open(filename, mode='w') as f:
                f.write(cls.to_json_string(dicted))

    @staticmethod
    def from_json_string(json_string):
        "Returns the list of the JSON repr json_string"
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        "Returns an instance with all attrs already set"
        dummy_attrs = cls(10)
        dummy_attrs = cls.update(**dictionary)
        return dummy_attrs

    @classmethod
    def load_from_file(cls):
        "Returns a list of instances"
        filename = f"{cls.__name__}.json"
        json_final = []
        if not os.path.exists(filename):
            return []
        with open(filename) as f:
            json_readed = json.read(f)
        json_str = cls.to_json_string(json_readed)
        for i in range(len(json_str)):
            json_final.append(cls.create(**json_str))
        return json_final
