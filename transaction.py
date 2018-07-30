import os
import sys

import configuration
import service


"""
Transaction module will loads all the configuration files and information of the game.
If you liked to change the service information, please change it in config/global.config file.
"""


def add_user(username):
    """
    Create a transaction that will add user to the database

    Parameter:
        username: name of the user (username) that will be added
    """
    pass


def reorder(username: str, new_order: int):
    """
    Reorder the user into different sequence

    Parameter:
        username: (String)
            username that need to be reorder

        new_order: (Integer)
            the new order that order to be
    """


def get_property_owner(property: list, **propertyId):
    """
    Parameter:
        property: (String List)
            Property name that doesn't know owner

        propertyId: (Integer List)
            ID of the property. ranged from 1 to 28
            **Internal use only**

    Return:
        player: (String)
            player's username that owns the property.
            If not owned, will return None
    """

    username = None
    return username


def get_balance(player):
    """
    Check player's money account
    """

    # Create transaction to check player money balance

    # Return the money amount
    money = 0
    return money


def transfer(player, new_player, property=list(), money=0):
    """
    Use to transfer money and/or property from player -> new player
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
        INTERNAL FUNCTION
        Check property ownership validation

        Return:
            1 if player owned that property, else 0
        """

        return 1 if (player == get_property_owner(property)) else 0

    def check_money(player, money):
        """
        INTERNAL FUNCTION
        Check money validation

        Return:
            1 if enough, else 0
        """
        return 1 if (money <= get_balance(player)) else 0


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
