CREATE TABLE Property
(
    name        TEXT(255)   PRIMARY KEY,
    type        TEXT(255)   NOT NULL,
    price       REAL     NOT NULL,
    mortgage    REAL     NOT NULL,
    house0      REAL,
    house1      REAL,
    house2      REAL,
    house3      REAL,
    house4      REAL,
    hotel       REAL,
    house_cost  REAL
);
