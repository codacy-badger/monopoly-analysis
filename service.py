# --- Module Import -----------------------------
import configuration

"""
Service Module
--------------
Service gives information and asks prompt from user
"""


def error(instance: object):
    """ Generate Error to user and then try not to break the program

    Args:
        instance:
    """
    print("{1}[ Error ]{2} > {0}".format(instance, '\x1b[6;30;41m', '\x1b[0m'))
    raise instance


def warning(instance: object):
    print("{1}[ Warning ]{2} > {0}".format(
        instance, '\x1b[6;30;43m', '\x1b[0m'))


def log(log_text):
    """

    Args:
        log_text:
    """
    print('\x1b[6;30;42m' + "[ Log ]" + '\x1b[0m' + " > " + log_text)


def announce(text: str):
    """ This function is used to format the program.

    Parameter:
        text: (String) the text that will be shown.
    """
    print("\nService > {}".format(text))

    return


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

    def user_prompt():
        announce("Please type in your player name. Press ENTER to stop")
        items = input()
        return items

    # Edit prompt() here ----------
    if type(prompt) != type("String"):
        raise ValueError

    if prompt == 'action':
        action_prompt(player)
    elif prompt == "confirm":
        confirm_prompt(player)
    elif prompt == 'user':
        return user_prompt()

    return
