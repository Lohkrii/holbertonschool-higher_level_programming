#!/usr/bin/python3
""" Creates an object from a JSON file """
import json


def load_from_json_file(filename):
    """ Creates an object from a JSON File """
    with open(filename) as holder:
        new_obj = json.load(holder)
        return new_obj
