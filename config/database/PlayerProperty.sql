CREATE TABLE PlayerProperty
(
    -- username stores the player that owns the property
    -- property stores the property owns by the player
    -- rent_price stores the current rent price, will be recalculated after every turn
    -- is_monopoly stores if that property must 2x the rent price
    -- house_count gives information about house count in the property. Range from 0-4. But if equals 5 -> have hotel
    -- is_mortgage store information if the property is in mortgage

    username TEXT,
    property TEXT,
    rent_price REAL,
    is_monopoly TEXT NOT NULL,
    house_count REAL NOT NULL,
    is_mortgage TEXT,

    CONSTRAINT PlayerProperty_username_property_pk
    PRIMARY KEY (username, property),

    CONSTRAINT PlayerProperty_Player_name_fk
    FOREIGN KEY (username)
    REFERENCES Player(username)
    ON DELETE CASCADE,

    CONSTRAINT PlayerProperty_Property_property_fk
    FOREIGN KEY (property)
    REFERENCES Property (property)
    ON DELETE CASCADE
);
