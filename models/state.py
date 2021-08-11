#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from os import getenv

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            list_cities = []
            for cities in all(City).values():
                if (cities.state_id) == self.id:
                    list_cities.append(cities)
            return list_cities
    else:
        cities = relationship("City", backref=("state"),
                              cascade="all, delete", passive_deletes=True)
