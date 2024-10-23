from setup_database import Base, engine
from sqlalchemy.orm import sessionmaker
from models import Person

# Create tables in the database, if already a table, just skip and not create again
Base.metadata.create_all(engine)

# Create the session
Session = sessionmaker(bind=engine)
session = Session()


p1 = Person(32598, "Anna", "Smith", "f", 25)
p2 = Person(32578, "Bob", "Cold", "m", 22)
p3 = Person(32520, "Angela", "Müller", "f", 30)

session.add(p1)
session.add(p2)
session.add(p3)

# Commit the transaction to save the user to the db
session.commit()

# # Find the user by name
# person_to_update = session.query(Person).filter_by(firstname = "Ana").first()
# Update User
# person_to_update.lastname = "Smith"   
# session.commit()


# # Delete
# person_to_delete = session.query(Person).filter_by(id = 2).first() 
# person_to_delete = session.query(Person).filter_by(id = 3).first() 

# session.delete(person_to_delete)
#session.commit()

# Query all users
users = session.query(Person).all()
for user in users:
    print(f"Person {user.id}: {user.firstname} {user.lastname}, {user.age} {user.gender}")