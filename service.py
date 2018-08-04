# --- Module Import -----------------------------
import configuration
import support

"""
Service Module
--------------
Service gives information and asks prompt from user
"""


def announce(text: str):
    """ This function is used to format the program.

    Parameter:
        text: (String) the text that will be shown.
    """
    print("Service > {}".format(text))

    return


def error(instance: object):
    """ Generate Error to user and then try not to break the program

    Args:
        instance:
    """
    print("[ ERROR ] > {}".format(instance))
    # raise SystemError


def warning(instance: object):
    """

    Args:
        instance:
    """
    print("[ Warning ] > {}".format(instance))


def prompt(player=None, prompt=None):
    """ Prompt user to do something to resolve background requests

    Parameter:
        player: (String)
            Username of the player that needs to resolve request

        prompt: (String)
            Custom text that other function wants to show to user

    Args:
        player:
        prompt:
    """

    def action_prompt(player: str):
        """ Send a prompt that requires user prompt

        Args:
            player:
            prompt:
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
        configuration.update('game_package', game_package)
        support.check_game_package_configuration()
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


def log(log_text):
    """

    Args:
        log_text:
    """
    print("[ Log ] > {}".format(log_text))
