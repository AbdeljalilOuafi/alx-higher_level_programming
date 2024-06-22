#!/usr/bin/python3
"""City Class"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)



