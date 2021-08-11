#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    import FileStorage
    storage = FileStorage()
    storage.reload()
