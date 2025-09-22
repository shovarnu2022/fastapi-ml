"""
> Helps auto-generate fields like ID
> Can make different attributes optional or use default values for specific tasks as required.
> Helps add validations specific to one operation without affecting others.
> Having explicit classes for each action makes the code self-explanatory
> makes it easier to debug and extend
"""

from sqlalchemy import Column, Integer, String
from database import Base


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

