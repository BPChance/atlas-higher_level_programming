#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1:4]

        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
        Session = sessionmaker(bind=engine)
        session = Session()

        cities = session.query(City).join(State).order_by(City.id).all()

        for city in cities:
            print(f"{city.state.name}: ({city.id}) {city.name}")

        session.close()
