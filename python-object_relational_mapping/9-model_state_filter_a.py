#!/usr/bin/env python3
""" list states with "a" in their name """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_a(username, password, database):
    """ connects to a MySQL database and lists all State objects containing the letter 'a' """
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    
    for state in states:
        print(f"({state.id}) {state.name}")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states_with_a(username, password, database)