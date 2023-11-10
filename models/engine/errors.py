#!/usr/bin/python3
"""this file defines errorsused in FileStorage and console"""


class ModelNotFoundError(Exception):
    """Raised if unknown module is passed"""
    def __init__(self, arg="BaseModel"):
        super().__init__("Model with name {} is not registered!".format(arg))


class InstanceNotFoundError(Exception):
    """Raised if unknown id is passed"""
    def __init__(self, obj_id="", arg="BaseModel"):
        super().__init__(
            "Instance of {} with id {} does not exist!".format(arg, obj_id))
