CREATE TABLE Player
(
  -- username store player username
  -- money stores player current money
  -- sequence stores player game sequence
  -- value stores player current value. calculated via money + all assets

  username TEXT PRIMARY KEY,
  money    REAL    NOT NULL,
  sequence INTEGER NOT NULL,
  value    REAL    NOT NULL
);
