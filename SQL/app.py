import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.jinja_env.filters['zip'] = zip

engine = create_engine('postgresql+psycopg2://postgres:test123@host.docker.internal:5432/postgres', pool_pre_ping= True)
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    try:
        flights = db.execute("SELECT * FROM flights").fetchall()
        origins = db.execute("SELECT city FROM airports").fetchall()
    finally:
        db.close()
    destinations = origins
    return render_template("index.html", flights=flights, origins = origins, destinations = destinations)

@app.route("/newflight", methods=["POST"])
def newflight():
    try:
        origin = request.form.get("flight_origin")
        destination = request.form.get("flight_destination")
    except ValueError:
        return render_template("error.html", message = "Something went wrong, please try again!")
    
    if db.execute("SELECT city FROM airports WHERE city IN (:o, :d)", {"o": origin, "d": destination}).rowcount != 2:
        return render_template("error.html", message = "One of the cities you selected isn't available. Please try again!")
    try:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, 99999999)", {"origin": origin, "destination":destination})
        db.commit()
    finally:
        db.close()
    return render_template("success.html", origin = origin, destination=destination)


@app.route("/requestedflights")
def requestedflights():
    try:
        reqflights = db.execute("SELECT origin, destination FROM flights WHERE duration = 99999999").fetchall()
    finally:
        db.close()
    return render_template("reqflights.html", flights = reqflights)

@app.route("/flights")
def flights():
    try:
        flights = db.execute("SELECT * FROM flights").fetchall()
    finally:
        db.close()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    try:
        flight = db.execute("SELECT f.id as id, f.origin as origin, a1.airportcode as ocode, f.destination as destination, a2.airportcode as dcode, f.duration as duration, f.duration/60 as dih FROM flights f INNER JOIN airports a1 ON a1.city = f.origin INNER JOIN airports a2 ON a2.city = f.destination WHERE f.id=:id", {"id":flight_id}).fetchone()
        if flight is None:
            return render_template("error.html", message="The flight you are looking for is not in our database 🙃")
    finally:
        db.close()
    return render_template("flight.html", flight_id=flight.id, flight_origin = flight.origin, flight_destination = flight.destination, ocode = flight.ocode, dcode = flight.dcode, flight_duration = flight.duration)