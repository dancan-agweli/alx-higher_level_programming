#!/usr/bin/python3
"""
Lists all City objects with their corresponding State names
from the 'hbtn_0e_101_usa' database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create a database connection
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query and print City objects with corresponding State names
    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()

