import configuration
import database

"""
Transaction Module
-----------------
Transaction module makes the actions into the pre SQL script.
"""


# --- Player / User Related Transaction ---------------------------------


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
    """

    Args:
        player:

    Returns:

    """
    return database.exists('Player', 'username', player)


def count_user():
    """

    Returns:

    """
    return database.select('COUNT(username)', 'Player')


# --- Property Transaction ----------------------------------------------


def buy_property(player, asset, price=None):
    """ Buy a property
    NOTE: Program will check for money. If not, it will raise TransactionError

    Args:
        player :
        asset :
        price :

    Raises:
        TransactionError :
    """
    pass


# def sell_property(player, property, price=None):
#     pass


def get_property(asset) -> str:
    """ Retrieve players property

    Args:
        asset: (String or String List) Property name that doesn't know owner


    Returns:
        player: (String) player's username that owns the property. If not owned, will return None
    """


def set_property(player, asset):
    """ Assign property to the player

    Args:
        player:
        asset:
    """

    pass


def transfer_property(player, new_player, asset):
    """
    Transfer property ownership

    Args:
        player:
        new_player:
        asset:
    """


# --- Money Transaction -------------------------------------------------


def get_money(player: str):
    """ Check player 's money account

    Args:
        player:
    """

    # Create transaction to check player money balance

    # Return the money amount
    pass


def set_money(player, money):
    """
    Set the money balance to the database

    Args:
        player:
        money:
    """
    pass


def add_money(player, money):
    pass


# --- House Transaction -------------------------------------------------


def buy_house(player, asset: str, money: int):
    """ Create a transaction when user want to buy a property
    """

    # Retrieve data from the database
    if player == get_property(asset):
        house_count = get_house(asset)

    # Data validation
    if (house_count <= 0) or (house_count >= 5):
        raise ValueError("Property cannot have more than 4 home")

    # Check property ownership + money + current house count

    # Check if any parameter is invalid

    # If still good, make transaction to database

    # return


def sell_house(player, property, amount):
    """
    """

    # Retrieve the data from the database
    database.select('*', 'PlayerAsset')

    # Data Input validation
    # if amount <= 0 or amount >= 5:
    #     raise ValueError("You cannot sell house that you do not own")

    # Check property ownership + money + current house count

    # Check if any parameter is invalid

    # If still good, make transaction to database


def get_house(asset):
    """
\
    Args:
        asset:

    Returns:

    """
    return int(database.select('house_count', 'PlayerAsset', 'propertyId', '=', asset))


def property_name_to_property_id(property_name):
    """

    Args:
        property_name:

    Returns:

    """
    return database.select('id', 'Asset', 'name', '=', property_name)


# --- Hotel Transaction -------------------------------------------------


def buy_hotel(player, asset):
    """ Buy a hotel to the property
    Will complete when user can buy the hotel
    NOTE: Will delete house, because following the hotel buy rule

    Args:
        player (String) : username that wants to buy a hotel
        asset: (String) : property to buy a hotel

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


def sell_hotel(player, asset):
    """ Sell the hotel to liquidify
    NOTE: 1 hotel = 5 house (in the need of selling the hotel)

    Args:
        player:
        asset:

    """

    # Check Data Validation

    # Check property eligibility

    # Check property hotel price

    # Check player money on hotel price

    # Create money transaction

    # Create property transaction
    pass


# --- Player Valuation Transaction --------------------------------------


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


# --- Mortgage Transaction ----------------------------------------------


def get_mortgage_status(asset):
    """ Get the mortgage status, based on <property> listings

    Args:
        asset:

    """
    pass


def set_mortgage_status(asset, status):
    """ Set the mortgage status to the property

    Args:
        asset: property to be set status with
        status: status that property will have
    """
    pass


def mortgage(player, asset):
    """ Mortgage the property and add money to player

    Args:
        asset:
        player:
    """
    pass


def remortgage(asset):
    """ Remortgage the property
    Args:
        asset:
    """
    pass


# Composite Transaction -------------------------------------------------


def transfer(player, new_player, asset=None, money=0):
    """ Transfer money and/or asset from player -> new player
    Args:
        player (String) : Player that starts the transfer
        new_player (String) : Player that will get the benefit from the transfer
        asset: (List)
            Lists of asset that will be transferred to new_player from player
            If left blank, asset will not be transferred.
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

    def check_property(player, asset):
        """ INTERNAL FUNCTION
        Check asset ownership validation
        Args:
            player:
            asset:
        Returns:
            1 if player owned that asset, else 0
        """

        return True if (player == get_property(asset)) else False

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

    # transfer() starts here
    if asset is None:
        asset = list()

    # Start coding transfer() here
    if len(asset) != 0:
        # Check each asset ownership
        pass

    if money != 0:
        # Check player's money balance
        if not check_money(player, money):
            raise TransactionError
        else:
            pass
            # transfer_money(player, new_player, money)


# --- Custom-defined Exception -------------------------------------------


class TransactionError(Exception):
    """Will rise when the transaction cannot be completed"""

    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors
