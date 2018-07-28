import os

import configuration
import service


def announce(text):
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


def error(instance):
    print("Service [ERROR] > {}".format(instance))
    return


def user_prompt(player=None, prompt=None):
    """

    :param player:
    :param prompt:
    :return:
    """
    if type(prompt) != type("String"):
        raise ValueError
        return

    if prompt == 'action':
        action_prompt(player=player)
    elif prompt == "confirm":
        confirm_prompt()
    elif prompt == 'package':
        package_prompt()

    return


def action_prompt(player):
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


def confirm_prompt(player=""):
    """

    :param player:
    :return:
    """
    print("{} > Are you sure?".format(player))
    result = bool(input())
    return result


def package_prompt():
    service.announce(
        "Welcome to Monopoly Analysis. Please choose the game package.")
    game_package = input()
    update_configuration('game_package', game_package)
    check_game_package_configuration()
    return


def update_configuration(key, value):
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
