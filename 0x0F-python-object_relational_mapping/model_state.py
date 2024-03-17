#!/usr/bin/python3
"""
Script that defines class states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    __tablename__ : Represent table of the class.
    id (int): Represent the id of the class.
    name (str): Represent state name of the class.
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
