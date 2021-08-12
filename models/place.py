#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from os import getenv
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy import *

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          "places.id"), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          "amenities.id"), primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    place_amenity

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            list_reviews = []
            for reviews in all(Review).values():
                if (reviews.place_id) == self.id:
                    list_reviews.append(reviews)
            return list_reviews

        @property
        def amenities(self):
            list_amenities = []
            for amenity in all(Amenity).values():
                if (amenity.place_id) == self.id:
                    list_amenities.append(amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, obj):
            if (obj.__class__ == Amenity):
                self.amenity_ids.append(Amenity.id)

    else:
        reviews = relationship("Review", backref="place",
                               cascade="all, delete", passive_deletes=True)
        amenities = relationship(
            "Amenity", secondary="place_amenity", viewonly=False)
