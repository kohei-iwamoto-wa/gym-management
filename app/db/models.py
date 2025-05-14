# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

class Bukken(Base):
    __tablename__ = 'bukken'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

class Kukaku(Base):
    __tablename__ = 'kukaku'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
