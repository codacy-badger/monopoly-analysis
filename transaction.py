import configuration
import database

"""
Transaction Module
-----------------
Transaction module makes the actions into the pre SQL script.
"""

""" --- Player / User Related Transaction --------------------------------- """


def add_user(username, sequence):
    """ Create a transaction that will add user to the database

    Args:
        username: name of the user (username) that will be added
        sequence:
    """
    money = configuration.CONFIG['starter_money']
    lists = [username, money, sequence, money]

    database.insert('Player', lists)
    pass


def delete_user(username):
    """ Delete the user from the database, because they have bankrupt or quit the game

    Args:
        username: (String) name of the user that will be deleted from Player table
    """
    pass


def reorder(username: str, new_order: int):
    """ Reorder the user into different sequence

    Args:
        username:
        new_order:

    """
    pass


def check_user(player):
    return database.exists('Player', 'username', player)


""" --- Property Transaction ---------------------------------------------- """


def buy_property(player, property, price=None):
    """ Buy a property
    NOTE: Program will check for money. If not, it will raise TransactionError

    Args:
        player :
        property :
        price :

    Raises:
        TransactionError :
    """
    pass


# def sell_property(player, property, price=None):
#     pass


def get_property(property) -> str:
    """ Retrieve players property

    Args:
        property: (String or String List) Property name that doesn't know owner


    Returns:
        player: (String) player's username that owns the property. If not owned, will return None
    """


def set_property(player, property):
    """ Assign property to the player

    Args:
        player:
        property:
    """

    pass


def transfer_property(player, new_player, property):
    """
    Transfer property ownership

    Args:
        player:
        new_player:
        property:
    """


""" --- Money Transaction ------------------------------------------------- """


def get_money(player: str):
    """ Check player 's money account

    Args:
        player:
    """

    # Create transaction to check player money balance

    # Return the money amount
    pass


def set_money(player, amount):
    """
    Set the money balance to the database

    Args:
        player:
        amount:
    """
    pass


def add_money(player, amount):
    pass


""" --- House Transaction ------------------------------------------------- """


def buy_house(player, property: str, amount: int):
    """ Create a transaction when user want to buy a property
    """

    # Data Input validation
    if amount <= 0 or amount >= 5:
        raise ValueError("Property cannot have more than 4 home")

    # Check property ownership + money + current house count

    # Check if any parameter is invalid

    # If still good, make transaction to database
    return


def sell_house(player, property, amount):
    """
    """

    # Data Input validation
    if amount <= 0 or amount >= 5:
        raise ValueError("You cannot sell house that you do not own")

    # Check property ownership + money + current house count

    # Check if any parameter is invalid

    # If still good, make transaction to database


""" --- Hotel Transaction ------------------------------------------------- """


def buy_hotel(player, property):
    """ Buy a hotel to the property
    Will complete when user can buy the hotel
    NOTE: Will delete house, because following the hotel buy rule

    Args:
        player (String) : username that wants to buy a hotel
        property (String) : property to buy a hotel

    Raises:
        TransactionError

    """

    # Check Data Validation

    # Check property ownership

    # Check property hotel price

    # Check player money on hotel price

    # Create money transaction

    # Add hotel to the property

    # Remove all home from property
    pass


def sell_hotel(player, property):
    """ Sell the hotel to liquidify
    NOTE: 1 hotel = 5 house (in the need of selling the hotel)

    Args:
        player:
        property:

    """

    # Check Data Validation

    # Check property eligibility

    # Check property hotel price

    # Check player money on hotel price

    # Create money transaction

    # Create property transaction
    pass


""" --- Player Valuation Transaction -------------------------------------- """


def update_value(player):
    """ Update player value from the database

    Args:
        player:
    """
    pass


def get_value(player):
    """ Get the player's value

    Args:
        player:
    """
    pass


def set_value(player, value):
    """ Set the value of the player with the value

    Args:
        player:
        value:
    """
    pass


""" --- Mortgage Transaction ---------------------------------------------- """


def get_mortgage_status(property):
    """ Get the mortgage status, based on <property> listings

    Args:
        property:
    """
    pass


def set_mortgage_status(property, status):
    """ Set the mortgage status to the property

    Args:
        property: property to be set status with
        status: status that property will have
    """
    pass


def mortgage(player, property):
    """ Mortgage the property and add money to player
    Args:
        player:
        property:
    Raise:
        TransactionError
    """
    pass


def remortgage(property):
    """ Remortgage the property
    Args:
        property:
    Raise:
        TransactionError
    """
    pass


""" Composite Transaction ------------------------------------------------- """


def transfer(player, new_player, property=None, money=0):
    """ Transfer money and/or property from player -> new player
    Args:
        player (String) : Player that starts the transfer
        new_player (String) : Player that will get the benefit from the transfer
        property: (List)
            Lists of property that will be transferred to new_player from player
            If left blank, property will not be transferred.
            If given incorrect property, will raised ValueError
        money: (Integer)
            Money that will be transferred to new_player from player
            If left blank or zero, money will not be transferred and raised ValueError
            If left negative, money will not be transferred and raised ValueError
    Raises:
        ValueError:
            Money data is not valid
            Property data is not valid
        TransactionException:
            Raised when transaction is not completed, resulted from errors
    """

    def check_property(player, property):
        """ INTERNAL FUNCTION
        Check property ownership validation
        Args:
            player:
            property:
        Returns:
            1 if player owned that property, else 0
        """

        return True if (player == get_property(property)) else False

    def check_money(player, money):
        """ INTERNAL FUNCTION
        Check money validation
        Args:
            player:
            money:
        Returns:
            1 if enough, else 0
        """
        return True if (money <= get_money(player)) else False

    if property is None:
        property = list()

    # Start coding transfer() here
    if len(property) != 0:
        # Check each property ownership
        pass

    if money != 0:
        # Check player's money balance
        if not check_money(player, money):
            raise TransactionError
        else:
            pass
            # transfer_money(player, new_player, money)


""" --- Self-defined Exception ------------------------------------------- """


class TransactionError(Exception):
    """Will rise when the transaction cannot be completed"""

    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors
