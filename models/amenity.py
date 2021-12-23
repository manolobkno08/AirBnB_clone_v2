#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models

if models.type_storage == "db":
    class Amenity(BaseModel, Base):
        """Class representation Amenity"""
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)

else:
    class Amenity(BaseModel):
        """Class representation Amenity"""
        name = ""
