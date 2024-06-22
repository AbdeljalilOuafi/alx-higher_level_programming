#!/usr/bin/python3
"""Fetch A state"""
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    result = session.query(City, State).filter(City.state_id == State.id).all()

    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
