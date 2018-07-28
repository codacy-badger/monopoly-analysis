import os

import configuration
import service
import database


def announce(text: str):
    """
    This function is used to format the program.

    Parameter:
        text: (String) the text that will be shown.
    """
    try:
        if isinstance(text, str):
            str(text)
    except Exception as inst:
        service.error(inst)

    print("Service > {}".format(text))

    return


def error(instance: object):
    print("Service [ERROR] > {}".format(instance))
    return


def prompt(player=None, prompt=None):
    """

    :param player:
    :param prompt:
    :return:
    """
    def action_prompt(player: str):
        """
        :param player:
        :return:
        """
        print("{} > Please choose action(s)".format(player))
        print("{}\t{}\t{}]\t{}".format(
            '[buy] Buy Property at full',
            '[auction] Auction Property',
            '[trade] Trade money or Property',
            '[done] Finished your turn'))
        return

    def confirm_prompt(player: str):
        """
        :param player:
        :return:
        """
        print("{} > Are you sure?".format(player))
        result = bool(input())
        return result

    def package_prompt(player: str):
        service.announce(
            "Welcome to Monopoly Analysis. Please choose the game package.")
        game_package = input()
        update_configuration('game_package', game_package)
        check_game_package_configuration()
        return

    def user_prompt():
        return

    # Edit prompt() here ----------
    if type(prompt) != type("String"):
        raise ValueError
        return

    if prompt == 'action':
        action_prompt(player)
    elif prompt == "confirm":
        confirm_prompt(player)
    elif prompt == 'package':
        return package_prompt(player)
    elif prompt == 'user':
        return user_prompt()

    return


def update_configuration(key: str, value):
    """
    For upgrading the information in configuration.
    WARNING: it does not update the real configuration file.

    :param key:
    :param value:
    :return:
    """
    if value != "":
        service.announce("Overriding '{}' from configuration".format(key))
        configuration.CONFIG[key] = value

    return


def check_game_package_configuration():
    """
    Use for checking the game package configuration.

    :return:
    """

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


def create_user(player):
    while True:
        username = service.prompt(prompt='user')

        if username == "":
            break

        # Save user in database
        database.insert('Player', player)
    return
