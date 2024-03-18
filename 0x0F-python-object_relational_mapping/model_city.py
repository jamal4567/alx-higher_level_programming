#!/usr/bin/python3
"""
Script that defines class states
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class State(Base):
    """
    __tablename__ : Represent table of the class.
    id (int): Represent the id of the class.
    name (str): Represent state name of the class.
    state_id (int): The state the city belongs to
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
