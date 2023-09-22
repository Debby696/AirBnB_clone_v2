#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

# Get value of the HBNB_TYPE_STORAGE environment variable
storage_type = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State inherits from BaseModel and Base """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """Getter function meant for Cities"""
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
