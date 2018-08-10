CREATE TABLE PlayerAsset
(
  -- username stores the player that owns the property
  -- property stores the property owns by the player
  -- rent_price stores the current rent price, will be recalculated after every turn
  -- is_monopoly stores if that property must 2x the rent price
  -- house_count gives information about house count in the property. Range from 0-4. But if equals 5 -> have hotel
  -- is_mortgage store information if the property is in mortgage

  username    TEXT,
  propertyId  TEXT,
  house_count REAL NOT NULL,
  hotel_conut REAL NOT NULL,
  is_monopoly TEXT NOT NULL,
  is_mortgage TEXT NOT NULL,
  rent_price  REAL NOT NULL,

  CONSTRAINT PlayerProperty_username_asset_pk
  PRIMARY KEY (username, propertyId),

  CONSTRAINT PlayerProperty_Player_name_fk
  FOREIGN KEY (username)
  REFERENCES Player (username)
    ON DELETE CASCADE,

  CONSTRAINT PlayerProperty_propertyId_id_fk
  FOREIGN KEY (propertyId)
  REFERENCES Asset (id)
    ON DELETE CASCADE
);
