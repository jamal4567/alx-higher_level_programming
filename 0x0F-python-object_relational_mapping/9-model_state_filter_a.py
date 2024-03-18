#!/usr/bin/python3
"""
This script prints every State object
That containe letter a
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()

    state_with_a = session.query(State).order_by(State.id).filter(State.name.like('%a%')).all()

    for state in state_with_a:
        print('{}: {}'.format(state.id, state.name))
