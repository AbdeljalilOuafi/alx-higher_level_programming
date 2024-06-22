#!/usr/bin/python3
"""Fetch all States"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter_by(name=argv[4]).one_or_none()
    if result is None:
        print("Not found")
    else:
        print("{}".format(result.id))
