#!/usr/bin/python3
""" Save an object to a JSON file """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object with json representation """
    with open(filename, "w") as holder:
        json.dump(my_obj, holder)
