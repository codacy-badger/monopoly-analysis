import os

# --- Module Import -----------------------------
# import configuration
# import database
import actions


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
        error(inst)

    print("Service > {}".format(text))

    return


def error(instance: object):
    print("Service [ERROR] > {}".format(instance))
    raise SystemError


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
        announce(
            "Welcome to Monopoly Analysis. Please choose the game package.")
        game_package = input()
        actions.update_configuration('game_package', game_package)
        actions.check_game_package_configuration()
        return

    def user_prompt():
        return

    # Edit prompt() here ----------
    if type(prompt) != type("String"):
        raise ValueError

    if prompt == 'action':
        action_prompt(player)
    elif prompt == "confirm":
        confirm_prompt(player)
    elif prompt == 'package':
        return package_prompt(player)
    elif prompt == 'user':
        return user_prompt()

    return
