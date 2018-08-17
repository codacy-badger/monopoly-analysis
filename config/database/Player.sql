CREATE TABLE Player (
  -- username store player username
  -- money stores player current money
  -- sequence stores player game sequence
  -- value stores player current value. calculated via money + all assets

  id       REAL PRIMARY KEY,
  username TEXT,
  money    REAL    NOT NULL,
  sequence INTEGER NOT NULL,
  value    REAL    NOT NULL DEFAULT 0
);
