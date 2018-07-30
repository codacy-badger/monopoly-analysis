import random

import service
import configuration
import transaction


def create_user():
    """
    Use for creating new user and add it into database
    """

    # Repeatedly prompt user for username input
    while True:
        username = service.prompt(prompt='user')

        if username == "":
            break

        # Save user in database
        transaction.add_user(username)
    return


def check_game_package_configuration():
    """
    Use for checking the game package configuration.
    """
    import os
    import configuration
    import service

    game_package = configuration.CONFIG['game_package']

    if not os.path.isdir("config/{}".format(game_package)):
        service.error("Path does not exists!")
        raise IOError

    for i in configuration.CONFIG['file_to_check']:
        if not os.path.exists("config/{}/{}".format(game_package, i)):
            service.error(
                "{} does not exists in game package folder!".format(i))
            raise IOError

    return


def roll_dice():
    """
    Roll 2 normal dice

    Return:
        result: (Integer)
            Result of the 2 dice
        dice_result: (Integer List)
            Individual result from 2 dice
    """
    def roll():
        """
        Using pseudo-random module from random module

        Return:
            individual_dice_result: (Integer)
                Range between 1 to 6
        """
        dice_face = configuration.CONFIG['dice_face']
        number = random.randint(0, len(dice_face))

        return dice_face[number]

    dice_result = list()
    result = 0

    for _ in range(2):
        individual_dice_result = roll()
        dice_result.append(individual_dice_result)
        result += individual_dice_result

    return result, dice_result
