# Database Configurations

There is a total of 3 database, shown below
"""
Player - 1 M - PlayerProperty - 1 1 - Property
"""

All of the CREATE script is in the ./config/database folder

## Player
`Player` database looks like this:
"""sql
CREATE TABLE Player(
    name        TEXT(255)   PRIMARY KEY,
    money       REAL        NOT NULL,
    sequence    INTEGER     NOT NULL
);
"""

## PlayerProperty
`PlayerProperty` looks like this
"""sql
CREATE TABLE PlayerProperty
(
    name        TEXT(255)   NOT NULL,
    property    TEXT(255)   PRIMARY KEY,

    CONSTRAINT PlayerProperty_Player_name_fk
    FOREIGN KEY (name) REFERENCES Player (name)
    ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT PlayerProperty_Property_property_fk
    FOREIGN KEY (property) REFERENCES Property (property)
    ON DELETE CASCADE ON UPDATE CASCADE
);
"""

## Property
`Property` looks like this
"""sql
CREATE TABLE Property
(
    name        TEXT(255)   PRIMARY KEY,
    type        TEXT(255)   NOT NULL,
    price       REAL        NOT NULL,
    mortgage    REAL        NOT NULL,
    house0      REAL,
    house1      REAL,
    house2      REAL,
    house3      REAL,
    house4      REAL,
    hotel       REAL,
    house_cost  REAL
);
"""
