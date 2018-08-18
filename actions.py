"""
Actions Module
--------------

Create, resolve issues in background.
Also runs the game (logic) in background after player's action.
"""

import math
import random

import configuration
import service
import transaction


# General Actions Handler ---------------------------------

def actions_handler(text):
    """ Will be triggered when user type in '/' commands

    Args:
        text:
    """

    def buy(command):
        """

        """
        if command is "":
            # transaction.buy_property()
            pass
        pass

    def mortgage(command):
        """

        """
        if command is "":
            # Do the mortgage process in current space

            # transaction.mortgage()
            pass
        else:
            # Use the given command parameter to mortgage the target asset

            # Check if the asset is valid

            # Check if the asset is users

            # Check if the asset id not mortgage

            # Check if the asset have no house/hotel on
            pass
        pass

    def upgrade(command):
        """ Upgrade the asset with house / hotel

        """
        try:
            # transaction.buy_house(command)
            pass
        except transaction.TransactionError:
            try:
                # transaction.buy_hotel()
                pass
            except transaction.TransactionError as inst:
                service.error("Cannot do any upgrades")
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
        """ Marked the input command with invalid.

        This method can be improved by adding the auto correct functionality

        Args:
            text:
        """
        service.warning("Command not found. Type /help for lists of command.")

    command = text.split(" ")[0]
    command_param = text[1:]

    if command == "/buy":
        buy(command_param)
    elif command == "/mortgage":
        mortgage(command_param)
    elif command == "/upgrade":
        upgrade(command_param)
    elif command == "/skip":
        skip()
    elif command == "/resolve":
        resolve()
    else:
        invalid(command_param)


# Player/User Related Actions -----------------------------


def create_user():
    """ Use for creating new user and add it into database
    NOTE: Will contact transaction.add_user() directly
    """

    sequence = 0
    # Repeatedly prompt user for username input
    while True:
        text_input = service.prompt(prompted_text="user")

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


# Suggestions / Decision Support Actions ------------------


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
    weight = configuration.CONFIG['liquidate_weight']


# Game play Actions ----------------------------------------


def generate_game(normal_game=True):
    """ Generate the game by getting game components

    Args:
        normal_game:

    """

    if normal_game:
        get_game_map()
        print_game_map(full=True)
        transaction.load_property('config/StandardAmerican/property.csv')


def get_game_map(file_path="config/{}".format(configuration.CONFIG['game_package'])):
    """
    Args:
        file_path:

    """

    tile_file_path = "{}/tiles.csv".format(file_path)

    global GAME_MAP
    GAME_MAP = dict()

    try:
        with open(tile_file_path, 'r+') as file:
            for i in file:
                GAME_MAP[str(i)] = None

    except FileNotFoundError:
        service.error("tiles.csv not found")
    except BaseException as inst:
        service.error(inst)


def print_game_map(full=False, max_tile=12, player_sequence=1):
    """ Prints the game map from a select <max_tile> scope
    Args:
        player_sequence:
        full:
        max_tile:
    """

    for tile_number in range(max_tile):
        # Retrieve the data
        current_player_location = transaction.get_location(player_sequence)
        property_id = ""
        property_name = ""
        property_price = "P"
        number_to_roll = 0

        # Check tile length
        text_length = 0

        # Choose color

        # Print tiles
        print("-" * math.ceil(text_length * 1.2))
        print(property_id)
        print(property_name)
        print("")
        print("")
        print(property_price)
        print(number_to_roll)


def roll_dice(normal_dice_count=2, speed_dice_count=0):
    """ Roll a dice. Any dice.
    This function also can roll a speed dice.

    Returns:
        result (Integer) : Result of the 2 dice
        dice_result (Integer List) : Individual result from 2 dice
    """

    def roll(dice_type: str):
        """ Random a dice face and return it's result

        Return:
            individual_dice_result: (Integer)
                Value that is in the dice (in configuration file)
        """
        dice_face = configuration.CONFIG[dice_type]
        number = random.randint(0, len(dice_face))

        return dice_face[number]

    # Initiate the dice rolling with placeholder variables
    dice_result = list()
    result = 0

    # Start rolling a dice, twice. and then store the result into the placeholder variables
    for _ in range(normal_dice_count):
        individual_dice_result = roll('dice_face')
        dice_result.append(individual_dice_result)
        result += individual_dice_result

    for _ in range(speed_dice_count):
        pass

    return result, dice_result
