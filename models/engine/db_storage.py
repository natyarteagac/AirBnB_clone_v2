#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.amenity import Amenity
from models.base_model import BaseModel
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
        """pass"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """pass"""
        Session = sessionmaker(self.__engine)
        self.__session = Session()

        if cls is None:
            state_id = session.query(
                User, State, City, Amenity, Place, Review).all()
        else:
            cls = eval(cls)
            new_dict = {}
            for alt_cls in session.query(cls).all():
                key = "{}.{}".format(alt_cls.name, alt_cls.id)
                new_dict.append(key, alt_cls)

        return new_dict

    def new(self, obj):
        """pass"""
        pass

    def save(self):
        """pass"""
        session.add()
        session.commit()

    def delete(self, obj=None):
        """pass"""
        pass

    def reload(self):
        """pass"""
        pass
