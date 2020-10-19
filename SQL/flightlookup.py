import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:test123@host.docker.internal:5432/postgres', pool_pre_ping= True)
db = scoped_session(sessionmaker(bind=engine))

def main():
    airportcodes = db.execute("SELECT airportcode FROM airports").fetchall()
    print(airportcodes)

    chosencode = input("Inserte el código del aeropuerto que desea revisar: ").upper()
    flights = db.execute("SELECT f.origin, f.destination, f.duration, a.airportcode FROM flights f INNER JOIN airports a ON f.origin = a.city OR f.destination = a.city WHERE a.airportcode = :airportcode ", {"airportcode": chosencode}).fetchall()
    print("Los vuelos disponibles de el aeropuerto seleccionado son: ")
    for flight in flights:
        print(f"Vuelo desde {flight.origin} hacia {flight.destination}. Duración: {flight.duration} minutos.")

    if flights is None or len(flights) == 0:
        print("El código seleccionado no tiene vuelos asociados.")
        return



if __name__ == "__main__":
    main()