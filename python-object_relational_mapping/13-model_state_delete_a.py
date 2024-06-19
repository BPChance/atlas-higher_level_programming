#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()
