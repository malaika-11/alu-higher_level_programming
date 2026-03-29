#!/usr/bin/python3
"""Print City objects with their related state names."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = (
        session.query(State.name, City.id, City.name)
        .join(City, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )
    for row in rows:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))

    session.close()
