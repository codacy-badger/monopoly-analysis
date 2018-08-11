import random

import configuration
import service
import transaction

"""
Actions Module
--------------
Create, resolve issues in background.
Also runs the game (logic) in background after player's action.
"""

"""
General Actions Handler
-----------------------
"""


def actions_handler(text):
    """ Will be triggered when user type in '/' commands

    Args:
        text:
    """

    def buy(text):
        """

        """
        pass

    def sell(text):
        """

        """
        pass

    def upgrade(text):
        """

        """
        pass

    def skip():
        """ Finish the player's turn
        """
        pass

    def resolve():
        """ Automatically resolve the situations, based on the current situation
        """
        pass

    def invalid(text):
        service.warning("Command not found. Type /help for lists of command.")

    text = text.split(" ")
    command = text[0]

    if command == "/buy":
        buy(text)
    elif command == "/sell":
        sell(text)
    elif command == "/upgrade":
        upgrade(text)
    elif command == "/skip":
        skip()
    elif command == "/resolve":
        resolve()
    else:
        invalid(text)


"""
Player/User Related Actions
---------------------------
"""


def create_user():
    """ Use for creating new user and add it into database
    NOTE: Will contact transaction.add_user() directly
    """

    sequence = 0
    # Repeatedly prompt user for username input
    while True:
        text_input = service.prompt(prompt="user")

        if text_input == "":
            break

        if text_input.startswith('/'):
            actions_handler(text_input)

        # If user pressed the ENTER without typing in any username, this function will finish itself.
        if text_input.isalnum():
            if not user_existed(text_input):
                # Create a transaction that adds a username to the game
                sequence += 1
                transaction.add_user(text_input, sequence)
            else:
                service.warning(text_input + " is already exists")
        else:
            service.warning(text_input + " contains non-character")

    # Finally, count how many players in the game.
    transaction.count_user()
    transaction.list_user()


def delete_user(username):
    """ Delete user from the service
    Just because they are bankrupt or quit the game during the gameplay.

    NOTE: Will contact transaction.remove_user() directly
    TODO: Need to resolve on how to deal with "quit during gameplay" user.

    Args:
        username:
    """
    pass


def user_existed(username):
    """ Check if user is existed by throwing instance to transaction.check_user()

    Args:
        username (String) : name of the user that wants to check existence

    Returns:
        transaction.check_user(username) result

    """
    return transaction.check_user(username)


"""
Suggestions / Decision Support Actions
--------------------------------------
"""


def suggest_liquidate(player: str, amount: int):
    """ Suggests player to sell property (or mortgage)
    This function can be triggered when player can't pay a rent or wants to liquidize the assets.

    By getting all the property from the database, and try to sell or mortgage properties.
    All possible calculations will later be weighted by

    - Methods of liquidation (like Mortgage or Sell)<br>
    - Monopoly bonus benefits<br>
    - Chance / Community Chest benefits<br>
    - Landing probability<br>

    Args:
        player (String) : player that wants to liquidate the property
        amount (Integer) : amount that need to be pay for rent (after making the money to 0)

    Returns:
        choice (List) : all possible ways to liquidate,
                        and given back the weight of each ones (more weight = better choice)
    """
    pass


"""
Gameplay Actions
----------------
"""


def generate_game():
    pass


def roll_dice():
    """ Roll a dice. Any dice.
    This function also can roll a speed dice.

    Returns:
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
