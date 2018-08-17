CREATE TABLE PlayerAsset (
  -- username stores the player that owns the property
  -- property stores the property owns by the player
  -- rent_price stores the current rent price, will be recalculated after every turn
  -- is_monopoly stores if that property must 2x the rent price
  -- house_count gives information about house count in the property. Range from 0-4. But if equals 5 -> have hotel
  -- is_mortgage store information if the property is in mortgage

  userId      TEXT,
  propertyId  TEXT,
  house_count REAL NOT NULL DEFAULT 0,
  hotel_count REAL NOT NULL DEFAULT 0,
  is_monopoly TEXT NOT NULL DEFAULT 'False',
  is_mortgage TEXT NOT NULL DEFAULT 'False',
  rent_price  REAL NOT NULL DEFAULT 0,

  CONSTRAINT PlayerProperty_username_asset_pk
  PRIMARY KEY (userId, propertyId),

  CONSTRAINT PlayerProperty_Player_name_fk
  FOREIGN KEY (userId)
  REFERENCES Player (id)
    ON DELETE CASCADE,

  CONSTRAINT PlayerProperty_propertyId_id_fk
  FOREIGN KEY (propertyId)
  REFERENCES Asset (id)
    ON DELETE CASCADE
);
