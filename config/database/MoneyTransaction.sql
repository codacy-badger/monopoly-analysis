CREATE TABLE MoneyTransaction (
  id               REAL PRIMARY KEY,
  playerWithdrawId TEXT NOT NULL,
  playerDepositId  TEXT NOT NULL,
  amount           REAL,
  turn             REAL,

  CONSTRAINT Fk_playerWithdrawId FOREIGN KEY (playerWithdrawId) REFERENCES Player (username),
  CONSTRAINT Fk_playerDepositId FOREIGN KEY (playerDepositId) REFERENCES Player(username)
);
