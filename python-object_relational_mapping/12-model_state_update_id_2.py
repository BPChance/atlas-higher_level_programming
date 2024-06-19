#!/usr/bin/python3
"""
update a State object
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

    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
