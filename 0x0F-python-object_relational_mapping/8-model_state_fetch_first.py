#!/usr/bin/python3
from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).order_by(State.id).first()

    if instance:
        print(f'{instance.id}: {instance.name}')
    else:
        print('Nothing')

    session.close()

