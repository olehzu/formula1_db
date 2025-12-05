use formula1_db;

show tables from formula1_db;

CREATE TABLE IF NOT EXISTS drivers (
    driverId INT PRIMARY KEY,
    driverRef VARCHAR(30),
    number VARCHAR(2),
    code VARCHAR(20),
    forename VARCHAR(30),
    surname VARCHAR(35),
    dob DATE,
    nationality VARCHAR(30),
    url VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS constructors (
	constructorId INT PRIMARY KEY,
    constructorRef VARCHAR(50),
    name VARCHAR(50),
    nationality VARCHAR(30),
    url VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS circuits (
    circuitId INT PRIMARY KEY,
    circuitRef VARCHAR(50),
    name VARCHAR(50),
    location VARCHAR(50),
    country VARCHAR(30),
    lat VARCHAR(15),
    lng VARCHAR(15),
    alt INT,
    url VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS races (
	raceId INT PRIMARY KEY,
    year INT,
    round INT,
    circuitId INT,
    name VARCHAR(50),
    date DATE,
    time TIME,
    url VARCHAR(255),
    
    FOREIGN KEY (circuitId) REFERENCES circuits(circuitId)
);


CREATE TABLE IF NOT EXISTS pitStops (
    raceId INT,
    driverId INT,
    stop INT,
    lap INT,
    time TIME,
    duration VARCHAR(20),
    milliseconds INT,
    
    PRIMARY KEY (raceId, driverId, stop),
   FOREIGN KEY (raceId) REFERENCES races(raceId),
   FOREIGN KEY (driverId) REFERENCES drivers(driverId)
);

CREATE TABLE IF NOT EXISTS results (
    resultId INT PRIMARY KEY,
    raceId INT,
    driverId INT,
    constructorId INT,
    number VARCHAR(2),
    grid VARCHAR(2),
    position VARCHAR(3),
    positionText VARCHAR(10),
    positionOrder varchar(2),
    points VARCHAR(2),
    laps VARCHAR(3),
    time VARCHAR(20),
    milliseconds VARCHAR(20),
    fastestLap INT,
    ranks INT,
    fastestLapTime VARCHAR(20),
    fastestLapSpeed DECIMAL(6,3),
    statusId INT,
    FOREIGN KEY (raceId) REFERENCES races(raceId),
	FOREIGN KEY (driverId) REFERENCES drivers(driverId),
    FOREIGN KEY (constructorId) REFERENCES constructors(constructorId) ON DELETE CASCADE on update set null
);

CREATE TABLE IF NOT EXISTS constructorStandings (
    constructorStandingsId INT PRIMARY KEY,
    raceId INT,
    constructorId INT,
    points INT,
    position INT,
    positionText VARCHAR(10),
    wins INT,
    FOREIGN KEY (raceId) REFERENCES races(raceId),
	FOREIGN KEY (constructorId) REFERENCES constructors(constructorId) on update set null on delete cascade
);

CREATE TABLE IF NOT EXISTS driverStandings (
    driverStandingsId INT PRIMARY KEY,
    raceId INT,
    driverId INT,
    points INT,
    position INT,
    positionText VARCHAR(10),
    wins INT,
   FOREIGN KEY (raceId) REFERENCES races(raceId),
	FOREIGN KEY (driverId) REFERENCES drivers(driverId)
);
















