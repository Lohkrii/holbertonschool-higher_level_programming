#!/usr/bin/python3
""" JSON object """


def from_json_string(my_str):
    """ Returns an object represented by a JSON string """
    obj = json.loads(my_str)
    return obj
