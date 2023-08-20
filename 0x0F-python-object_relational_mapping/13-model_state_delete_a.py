#!/usr/bin/python3
"""
Deletes State objects with 'a' in name from 'hbtn_0e_6_usa' database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a database connection
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()

    # Query and delete States with 'a' in name
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)

    # Commit the changes to the database
    session.commit()
    
    # Close the session
    session.close()

