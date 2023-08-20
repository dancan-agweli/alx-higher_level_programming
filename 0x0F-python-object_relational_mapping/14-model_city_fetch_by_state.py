#!/usr/bin/python3
"""
Prints all City objects from the 'hbtn_0e_14_usa' database.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Create a database connection"""
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    """ Create a session"""
    session = Session()

    """Query for City objects with related State objects"""
    query = session.query(City, State).join(State)

    """Print City information"""
    for city, state in query.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    """Commit and close the session"""
    session.commit()
    session.close()

