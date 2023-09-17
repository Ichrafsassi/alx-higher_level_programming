#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()

    print("Nothing" if state is None else f"{state.id}: {state.name}")
