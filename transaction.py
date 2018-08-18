"""
Transaction Module
-----------------

Transaction module makes the actions into the pre SQL script.
"""

import configuration
import database
import service


# --- Player / User Related Transaction ---------------------------------


def add_user(username, sequence):
    """ Create a transaction that will add user to the database

    Args:
        username: name of the user (username) that will be added
        sequence:
    """
    starter_money = configuration.CONFIG['starter_money']

    database.insert(table_name='Player', values=[username, starter_money, sequence, starter_money])


def delete_user(username: str):
    """ Delete the user from the database, because they have bankrupt or quit the game

    Args:
        username (str): name of the user that will be deleted from Player table
    """

    database.delete(table_name='Player', ref_column_name='name', ref_values='username')


def reorder_user(username: str, new_order: int):
    """ Reorder the user into different sequence

    Args:
        username (str):
        new_order (int):

    """
    pass


def check_user(player):
    """ Check that the username is duplicated or not

    Args:
        player:
    """

    return database.exists(table_name='Player', column_name='username', quantity=player)


def count_user():
    """ Count user that is in the game

    Returns:
        result from database.count()
    """

    return database.count('Player')


def list_user():
    """ List the user that is in the game

    Returns:
        result from database.select('username', 'Player')
    """

    return database.select(column_name='username', table_name='Player')


# --- Property Transaction ----------------------------------------------


def buy_property(player, asset, price=None):
    """ Buy a property that is not currently owned

    NOTE: Program will check for money. If not, it will raise TransactionError

    Args:
        player :
        asset :
        price :

    Raises:
        TransactionError :
    """
    pass


def sell_property(player, asset, price=None):
    """ Sell property that player IS OWNING

    Args:
        player:
        asset:
        price:
    """

    # Check property ownership

    # Check if the property have home / hotel inside
    database.select(column_name='house_count', table_name='PlayerAsset')

    # Start the transaction
    pass


def get_location(user_sequence):
    """ Get the user location from user sequence

    Args:
        user_sequence:

    Returns:

    """
    return database.select(column_name='location',
                           table_name='Player',
                           ref_column_name='sequence',
                           operator='=',
                           quantity=user_sequence)


def get_property(asset) -> str:
    """ Retrieve player that owns the <asset>

    Args:
        asset: (String or String List) Property name that doesn't know owner


    Returns:
        player: (String) player's username that owns the property. If not owned, will return None
    """
    # return database.select(column_name='')


def set_property(player, asset):
    """ Assign <asset> to the <player>

    Args:
        player:
        asset:
    """

    pass


def transfer_property(player, new_player, asset):
    """ Transfer property's ownership

    Args:
        player:
        new_player:
        asset:
    """
    pass


# --- Money Transaction -------------------------------------------------


def get_money(player: str) -> float:
    """ Check player money balance

    Args:
        player:
    """

    # Create transaction to check player money balance

    # Return the money amount
    pass


def set_money(player: str, money):
    """ Set the money balance to the database

    This method is different from transaction.add_money that, this SET the new value
    While the add_money increases the money

    Args:
        player (str): name of the user (not ID)
        money (float or int): money that will be set
    """

    database.update(table_name='Player', set_column_name='money', set_column_quantity=money, ref_column='name',
                    ref_column_quantity=player)


def add_money(player, money):
    """ Add money to the player in specific amount

    Args:
        player:
        money:
    """

    database.update(table_name='Player', set_column_name='money', set_column_quantity='money + {}'.format(money),
                    ref_column='name', ref_column_quantity=player)


# --- House Transaction -------------------------------------------------


def buy_house(player, asset: str, money: int):
    """ Create a transaction when user want to buy a property

    Args:
        player:
        asset:
        money:
    """

    # Retrieve data from the database
    house_count = get_house(asset) if player == get_property(asset) else 0

    # Data validation
    if (house_count <= 0) or (house_count >= 5):
        raise ValueError("Property cannot have more than 4 home")

    # Check property ownership + money + current house count

    # Check if any parameter is invalid

    # If still good, normalized some parameters
    asset = property_name_to_property_id(asset)

    # If still good, make transaction to database
    database.update(table_name='PlayerAsset', set_column_name='house_count', set_column_quantity=house_count,
                    ref_column='asset_id', ref_column_quantity=asset)

    # return


def sell_house(player, asset, amount):
    """ Sell the house, at a fixed rate

    Notes: House reselling rate is in the configuration file. You can edit it.

    Args:
        player:
        asset:
        amount:
    """

    # Retrieve the data from the database
    database.select(column_name='*', table_name='PlayerAsset')

    # Data Input validation
    # if amount <= 0 or amount >= 5:
    #     raise ValueError("You cannot sell house that you do not own")

    # Check property ownership + money + current house count

    # Check if any parameter is invalid

    # If still good, make transaction to database


def get_house(asset):
    """ Get house count from the asset given

    Args:
        asset:
    """
    return int(
        database.select(column_name='house_count', table_name='PlayerAsset', ref_column_name='propertyId', operator='=',
                        quantity=asset))


def property_name_to_property_id(property_name):
    """ Convert the property name to id (for database queries)

    Args:
        property_name:
    """
    return database.select(column_name='id', table_name='Asset', ref_column_name='name', operator='=',
                           quantity=property_name)


# --- Hotel Transaction -------------------------------------------------


def buy_hotel(player, asset):
    """ Buy a hotel to the property

    Complete when user can buy the hotel
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
    """ Sell the hotel to liquidise

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
    """ Get the mortgage status based on <asset> input listing

    Args:
        asset:

    """
    return bool(database.select(column_name='is_mortgage', table_name='PlayerAsset'))


def set_mortgage_status(asset: str, status: bool):
    """ Set the mortgage status to the property

    Args:
        asset: property to be set status with
        status: status that property will have
    """
    database.update(table_name='PlayerAsset', set_column_name='is_mortgage', set_column_quantity=status,
                    ref_column='assetId', ref_column_quantity=property_name_to_property_id(asset))


def mortgage(player, asset):
    """ Mortgage the property and add money to player

    Args:
        asset:
        player:
    """
    # database.update(set_column_name='is_mortgage', table_name='PlayerAsset', set_column_quantity='True')


def remortgage(asset):
    """ Remortgage the property

    Args:
        asset:
    """
    pass


# Composite Transaction -------------------------------------------------


def transfer(player, new_player, asset: list = None, money: float = 0):
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

    def check_property_validation(username, property_name):
        """ Check asset ownership validation

        Args:
            username:
            property_name:

        Returns:
            1 if player owned that asset, else 0
        """

        return True if (username == get_property(property_name)) else False

    def check_money_validation(username, money_value):
        """ Check money validation

        Args:
            username:
            money_value:

        Returns:
            1 if enough, else 0
        """
        return True if (money_value <= get_money(username)) else False

    def do_transaction(sender_player, receive_player, asset: list, money: float):
        """

        Args:
            sender_player:
            receive_player:
            asset:
            money:
        """
        pass

    # transaction.transfer() starts here ----------------------------
    if asset is None:
        asset = list()

    # Start coding transfer() here
    if len(asset) != 0:
        # Check each asset ownership
        pass

    if money != 0:
        # Check player's money balance
        if not check_money_validation(player, money) \
                or not check_property_validation(player, asset):
            raise TransactionError
        else:
            # Start the real transaction process
            pass
            # transfer_money(player, new_player, money)


def load_property(asset_reference_file):
    """

    Args:
        asset_reference_file:
    """
    try:
        file = open(asset_reference_file, 'r')

        for line in file:

            # Remove the line that have no id
            if not line[0].isnumeric():
                continue

            # Remove all space + convert to list
            line = line.replace(' ', '').split(',')

            # Insert the record to the database
            database.insert('Asset', line)

    except IOError:
        service.error('Cannot load property file')


# --- Custom-defined Exception -------------------------------------------


class TransactionError(Exception):
    """ Will rise when the transaction cannot be completed
    """

    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors
