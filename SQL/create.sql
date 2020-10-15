CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

CREATE TABLE airports (
    id SERIAL PRIMARY KEY,
    city VARCHAR NOT NULL,
    airportcode VARCHAR(3) NOT NULL
);