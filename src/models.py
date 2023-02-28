import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Vehicles(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(256))
    passengers = Column(String(256))
    length = Column(String(256))
    favorite_vehicle = relationship("Favorite")

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(256))
    population = Column(Integer)
    orbital_period = Column(String(256))
    rotation_period = Column(String(256))
    diameter = Column(String(256))
    favorite_planet = relationship("Favorite")

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    gender = Column(String(250))
    favorite_character = relationship("Favorite")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_fav = Column(Integer,ForeignKey('character.id'))
    planet_fav = Column(Integer,ForeignKey('planet.id'))
    vehicle_fav = Column(Integer,ForeignKey('vehicle.id'))
    character_relation = relationship ('Character', back_populates = 'favorite_character')
    vehicle_relation = relationship ('Vehicle', back_populates = 'favorite_vehicle')
    planet_relation = relationship ('Planet', back_populates = 'favorite_planet')
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
