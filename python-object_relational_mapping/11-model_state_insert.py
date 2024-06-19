#!/usr/bin/python3
""" adds the State object "Louisiana" to the database hbtn_0e_6_usa """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1:4]

        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        
        print(new_state.id)

        session.close()
