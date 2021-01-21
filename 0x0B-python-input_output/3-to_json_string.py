#!/usr/bin/python3
import json
""" JSON Representation of an object """


def to_json_string(my_obj):
    """ Returns JSON representation """
    rep = json.dumps(my_obj)
    return rep
