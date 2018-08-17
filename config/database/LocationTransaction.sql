CREATE TABLE LocationTransaction (
  -- id
  -- old_location
  -- new_location
  -- dice_rolls
  -- turns

  id           TEXT PRIMARY KEY,
  old_location REAL,
  new_location REAL,
  dice_rolls   TEXT,
  turns        REAL,

  CONSTRAINT FK_old_location FOREIGN KEY (old_location) REFERENCES Asset (id),
  CONSTRAINT FK_new_location FOREIGN KEY (new_location) REFERENCES Asset (id)

);
