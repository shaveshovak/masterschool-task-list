from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local SQLite database.
engine = create_engine('sqlite:///persons.db', echo=True)

# Define the base class for our classes (models) to inherit
Base = declarative_base()

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine)

# Create a session
session = SessionLocal()
