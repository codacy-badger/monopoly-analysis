CREATE TABLE PlayerProperty
(
    name        TEXT(255)   NOT NULL,
    property    TEXT(255)   PRIMARY KEY,
    
    CONSTRAINT PlayerProperty_Player_name_fk 
    FOREIGN KEY (name) REFERENCES Player (name) 
    ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT PlayerProperty_Property_property_fk 
    FOREIGN KEY (property) REFERENCES Property (property) 
    ON DELETE CASCADE ON UPDATE CASCADE
);