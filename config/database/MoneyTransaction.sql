CREATE TABLE MoneyTransaction (
  moneyTransactionId REAL PRIMARY KEY,
  playerWithdraw     TEXT,
  playerDeposit      TEXT,
  amount             REAL,
  rollCountId        REAL
);
