import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
print(os.getcwd())

engine = create_engine('postgresql+psycopg2://postgres:test123@host.docker.internal:5432/postgres', pool_pre_ping= True)
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)", {"origin":origin, "destination":destination, "duration":duration})
        print(f"Added flight from {origin} to {destination} with duration of {duration} minutes into flights table.")
    db.commit()


if __name__ == "__main__":
    main()