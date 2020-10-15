INSERT INTO flights(origin, destination, duration) VALUES('NEW YORK', 'LONDON', 415);
INSERT INTO flights(origin, destination, duration) VALUES('NEW YORK', 'LOS ANGELES', 360);
INSERT INTO flights(origin, destination, duration) VALUES('BUENOS AIRES', 'LONDON', 795);
INSERT INTO flights(origin, destination, duration) VALUES('CARACAS', 'TOKYO', 1680);
INSERT INTO flights(origin, destination, duration) VALUES('MILAN', 'BEIJING', 750);
INSERT INTO flights(origin, destination, duration) VALUES('WASHINGTON DC', 'BRISBANE', 1620);
INSERT INTO flights(origin, destination, duration) VALUES('WELLINGTON', 'SANTIAGO', 1980);

--UPDATE flights SET duration = 430 WHERE ORIGIN = 'NEW YORK' AND destination = 'LONDON';

--DELETE FROM flights WHERE destination = 'BOGOTA';

--SELECT SUM(duration), origin FROM flights GROUP BY origin HAVING COUNT(*) > 1;

INSERT INTO airports (city, airportcode) VALUES ('CARACAS', 'CCS');
INSERT INTO airports (city, airportcode) VALUES ('BUENOS AIRES', 'BAI');
INSERT INTO airports (city, airportcode) VALUES ('WASHINGTON DC', 'DCA');
INSERT INTO airports (city, airportcode) VALUES ('NEW YORK', 'JFK');
INSERT INTO airports (city, airportcode) VALUES ('WELLINGTON', 'WLG');
INSERT INTO airports (city, airportcode) VALUES ('TOKYO', 'HND');
INSERT INTO airports (city, airportcode) VALUES ('LONDON', 'LCY');
INSERT INTO airports (city, airportcode) VALUES ('BEIJING', 'PEK');
INSERT INTO airports (city, airportcode) VALUES ('BRISBANE', 'BNE');
INSERT INTO airports (city, airportcode) VALUES ('SANTIAGO', 'SCL');
INSERT INTO airports (city, airportcode) VALUES ('MILAN', 'MXP');