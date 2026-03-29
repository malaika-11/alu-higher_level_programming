#!/usr/bin/python3
"""Module that defines the Base class."""

import json


class Base:
    """Base class for all geometric models in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base with optional id or auto-incremented id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of a list of dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON serialization of objects to <ClassName>.json."""
        filename = "{}.json".format(cls.__name__)
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return list represented by a JSON string."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create instance with all attributes already set via update."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return list of instances loaded from <ClassName>.json file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(content)
        return [cls.create(**obj_dict) for obj_dict in list_dicts]
