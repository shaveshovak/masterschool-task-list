from sqlalchemy import Column, Integer, String, CHAR
from setup_database import Base

class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    gender = Column(CHAR)
    age = Column(Integer)

    def __init__(self, id, firstname, lastname, gender, age):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.id}) {self.firstname}  {self.lastname} {self.gender} {self.age}"