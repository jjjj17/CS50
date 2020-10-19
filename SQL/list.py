import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:test123@host.docker.internal:5432/postgres', pool_pre_ping= True)
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    print(type(flights))
    for flight in flights:
        print(f"El vuelo salió de {flight.origin} y llegó a {flight.destination} luego de {flight.duration} minutos")


if __name__ == "__main__":
    main()