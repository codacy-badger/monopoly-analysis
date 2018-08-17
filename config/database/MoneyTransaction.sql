CREATE TABLE MoneyTransaction (
  -- id
  -- turn
  -- withdraw_player_id
  -- deposit_player_id
  -- amount

  id                 REAL PRIMARY KEY,
  withdraw_player_id TEXT NOT NULL,
  deposit_player_id  TEXT NOT NULL,
  turn               REAL,
  amount             REAL,

  CONSTRAINT Fk_withdraw_player_id FOREIGN KEY (withdraw_player_id) REFERENCES Player (id),
  CONSTRAINT Fk_deposit_player_id FOREIGN KEY (deposit_player_id) REFERENCES Player (id)
);
