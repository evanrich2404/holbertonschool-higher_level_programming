#!/usr/bin/python3
"""The State Class Module"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """The State Class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
