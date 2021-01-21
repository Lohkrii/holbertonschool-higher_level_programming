#!/usr/bin/python3
""" JSON Representation of an object """
import json


def to_json_string(my_obj):
    """ Returns JSON representation """
    rep = json.dumps(my_obj)
    return rep
