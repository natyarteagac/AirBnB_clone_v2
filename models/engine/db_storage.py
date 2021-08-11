#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """pass"""

    __engine = None
    __session = None

    def __init__(self):
        """Creating the engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Takes the required query from created classes"""
        new_dict = {}

        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            for single_class in classes:
                list_class = self.__session.query(single_class).all()
            for key, value in list_class:
                new_dict.append(list_class)
        else:
            list_class = self.__session.query(cls).all()
            for objects in list_class:
                new_dict.update(
                    {objects.__class__.__name__ + "." + objects.id: objects})
        return new_dict

    def new(self, obj):
        """Create a new of object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit the changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the object if is not none"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create a session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker
                                 (self.__engine, expire_on_commit=False))
        self.__session = Session()
