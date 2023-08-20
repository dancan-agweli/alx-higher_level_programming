#!/usr/bin/python3
"""
Changes the name of State with id 2 to 'New Mexico' in 'hbtn_0e_6_usa'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("State with ID 2 not found in the database.")
    
    session.close()

