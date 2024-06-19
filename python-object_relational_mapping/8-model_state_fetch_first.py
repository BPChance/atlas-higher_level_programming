#!/usr/bin/python3
""" First state """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state(username, password, database):
    """ connects to a MySQL database and prints the first State object """
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"({state.id}) {state.name}")
    else:
        print("Nothing")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        print_first_state(username, password, database)
