"""
create_engine() -> Establishes the connection to the DB
Here, it connects to SQLite file named test.db

connect_args: SQLite-specific to allow connection sharing across threads

sessionmaker:
> Helps create new DB sessions
> Each session represents a transactional scope to the DB
> autoflush=False:
  SQLAlchemy will not automatically flush changes to the DB unless explicitly committed or refreshed
> autocommit=False:
  Disables automatic commit after each query
  commit manually to control transactions

declarative_base():
> creates a base class for models to inherit from, linking the python classes with DB tables.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

