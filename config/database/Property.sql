CREATE TABLE Property
(
  -- propertyId stores property location (1 is for Brown property that next to GO)
  -- propertyColor stores propery color
  -- propertyColorId stores property location, based on color
  -- name stores property name
  -- type stores property type (eg. 'Utility', 'Transport', 'Site')
  -- price stores property selling price
  -- mortgage stores property mortgage price
  -- house0 stores property rent with 0 home
  -- house1 stores property rent with 1 home
  -- house2 stores property rent with 2 home
  -- house3 stores property rent with 3 home
  -- house4 stores property rent with 4 home
  -- hotel stores property rent with hotel

  propertyID      REAL PRIMARY KEY,
  propertyColor   TEXT NOT NULL,
  propertyColorId REAL NOT NULL,
  name            TEXT NOT NULL,
  type            TEXT NOT NULL,
  price           REAL NOT NULL,
  mortgage        REAL NOT NULL,
  house0          REAL,
  house1          REAL,
  house2          REAL,
  house3          REAL,
  house4          REAL,
  hotel           REAL,
  house_cost      REAL,

  CONSTRAINT PropertyUnique
  UNIQUE (name, house0, house1, house2, house3, house4, hotel)
);
