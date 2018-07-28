import os
import sys

import configuration
import service


"""
Transaction module will loads all the configuration files and information of the game.
If you liked to change the service information, please change it in config/global.config file.
"""


def get_property_owner(property):
    """
    Return:
        player: (String)
            player's username that owns the property.
            If not owned, will return None
    """

    # return None
    pass


def transfer(player, new_player, property=list(), money=0):
    """
    Parameter:
        player: (String)
            Player that starts the transfer

        new_player: (String)
            Player that will get the benefit from the transfer

        property: (List)
            Lists of property that will be transfered to new_player from player
            If left blank, property will not be transfered.
            If given incorrect property, will raised ValueError

        money: (Integer)
            Money that will be transfered to new_player from player
            If left blank or zero, money will not be transfered and raised ValueError
            If left negative, money will not be transfered and raised ValueError

    Return:
        none

    Exception:
        ValueError:
            Money data is not valid
            Property data is not valid
        TransactionException:
            Raised when transaction is not completed, resulted from errors
    """
    # Check Property Data Validation
    try:
        for i in range(property):

            if isinstance(property[i], str):
                continue
            else:
                property[i] = str(property[i])

    except Exception:
        service.announce("Transaction failed. Property is not a string")
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


def buy_property(player, property, price=None):
    pass


def sell_property(player, property, price=None):
    pass


def buy_house(player, property, amount):

    # Data Input validation
    if (amount <= 0 or amount >= 5):
        raise ValueError

    pass


def sell_house(player, property, amount):
    # Data Input validation
    if (amount <= 0 or amount >= 5):
        raise ValueError

    pass


def buy_hotel(player, property):
    """
    The user buy the hotel from the property
    """

    # Check Data Validation

    # Check property eligibility

    # Check property hotel price

    # Check player money on hotel price

    # Create money transaction

    # Create property transaction
    pass


def sell_hotel(player, property):

    # Check Data Validation

    # Check property eligibility

    # Check property hotel price

    # Check player money on hotel price

    # Create money transaction

    # Create property transaction
    pass
