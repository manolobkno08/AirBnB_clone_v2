#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey

import models

if models.type_storage == "db":
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey(
            "states.id"), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="delete")
else:
    class City(BaseModel):
        """ The city class, contains state ID and name """
        state_id = ""
        name = ""
