import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:test123@host.docker.internal:5432/postgres', pool_pre_ping= True)
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("newairportcodes.csv")
    reader = csv.reader(f)
    for city, airportcode in reader:
        db.execute("INSERT INTO airports (city, airportcode) VALUES (:city, :airportcode)", {"city":city, "airportcode":airportcode})
        print(f"Added code {airportcode} as {city} airport code into airports table.")
    db.commit()


if __name__ == "__main__":
    main()