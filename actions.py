import os
import random

import service
import configuration
import transaction

"""
Actions Module
--------------
Create, resolve issues in background.
Also runs the game (logic) in background after player's action.
"""


"""
Player/User Related Actions
---------------------------
"""


def create_user():
    """ Use for creating new user and add it into database
    NOTE: Will contact transaction.add_user() directly
    """

    # Repeatedly prompt user for username input
    while True:
        username = service.prompt(prompt='user')

        if username == "":
            break

        # Create a transaction that adds a username to the game
        transaction.add_user(username)
    return


def delete_user():
    """ Delete user from the service
    Just because they are bankrupt or quit the game during the gameplay.
    NOTE: Will contact transaction.remove_user() directly
    TODO: Need to resolve on how to deal with "quit during gameplay" user.
    """
    pass


"""
Suggestions / Decision Support Actions
--------------------------------------
"""


def suggest_liquidate(player: str, amount: int):
    """ Suggests player to sell property (or mortgage) when the cash is not enough

    By getting all the property from the database, and try to sell or mortgage properties.
    All possible calculations will later be weighted by
    - Methods of liquidation (like Mortgage or Sell)
    - Monopoly bonus benefits
    - Chance / Community Chest benefits
    - Landing probability

    Args:
        player (String) : player that wants to liquidate the property
        amount (Integer) : amount that need to be pay for rent (after making the money to 0)

    Returns:
        choice (List) : all possible ways to liquidate, and given back the weight of each ones (more weight is better deals)
    """
    pass


"""
Gameplay Actions
----------------
"""


def roll_dice():
    """ Roll 2 normal dice

    Return:
        result (Integer) : Result of the 2 dice
        dice_result (Integer List) : Individual result from 2 dice
    """
    def roll():
        """ Random a dice face and return it's result

        Return:
            individual_dice_result: (Integer)
                Value that is in the dice (in configuration file)
        """
        dice_face = configuration.CONFIG['dice_face']
        number = random.randint(0, len(dice_face))

        return dice_face[number]

    # Initiate the dice rolling with placeholder variables
    dice_result = list()
    result = 0

    # Start rolling a dice, twice. and then store the result into the placeholder variables
    for _ in range(2):
        individual_dice_result = roll()
        dice_result.append(individual_dice_result)
        result += individual_dice_result

    return result, dice_result
