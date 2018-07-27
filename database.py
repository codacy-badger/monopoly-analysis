import sqlite3

DATABASE = None

def connect_database(db_src = 'config/StandardAmerican/property.db'):
    DATABASE = sqlite3.connect(db_src)    
    return

def get_property_owner(property):
    """
    Return:
        player: (String) 
            player's username that owns the property.
            If not owned, will return None
    """

    # return None
    pass

def transfer(player, 
            new_player,
            property = list(), 
            money = 0):
    """
    Parameter: 
        property: (List) 
            Lists of property that will be transfered to new_player from player
            If left blank, property will not be transfered.

        money: (Integer) 
            Money that will be transfered to new_player from player
            If left blank, money will not be transfered

    Return:
        none

    Exception:
        TransactionException: 
            Raised when transaction is not completed, resulted from errors
    """ 
    # try:
    #     # Start the transaction methods
    # catch PropertyException:
    #     pass
    # catch MoneyException:
    pass
    
    def check_property(player, property):
        """
        Exception:
            PropertyException: 
                Raised when player do not own one of the property.
        """
        # Start the query from player, 
        # SELECT name FROM property_owner WHERE property == property

        # If query failed, raise PropertyException
        pass
        

    def check_money(player, money):
        """
        Exception:
            MoneyException: 
                Raised when player do not have enough money.
        """
        # Start the query from player
        # SELECT money from player WHERE name = player

        # If query result is lower than money, raise MoneyException
        pass
        