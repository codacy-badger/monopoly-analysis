# --- Module Import -----------------------------
import service

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

    def action(player: str):
        """ Send a prompt that requires user

        Args:
            player:
        """
        print("{} > Please choose action(s)".format(player))
        print("{}\t{}\t{}".format(
            '[ /roll ] Roll a dice',
            '[ /upgrade ] Buy house/hotel on a property',
            '[ /auto ] Automatically make a decision'))

    def resolve(player: str):
        print("{} > Please choose action(s)".format(player))
        print("{}\t{}\t{}]\t{}\t{}".format(
            '[ /buy ] Buy Property at full price',
            '[ /auction ] Auction this property',
            '[ /trade ] Trade money or Property',
            '[ /done ] Finished your turn',
            '[ /auto ] Automatically make a decision'))

    def confirm(player: str):
        """
        :param player:
        :return:
        """
        print("{} > Are you sure?".format(player))
        result = bool(input())
        return result

    def user():
        announce("Please type in your player name. Press ENTER to stop")
        items = input()
        return items

    # Edit prompt() here ----------
    if not isinstance(type(prompt), str):
        service.error("Action is not string format")
        raise ValueError

    if prompt == 'action':
        action(player)
    elif prompt == 'resolve':
        resolve(player)
    elif prompt == "confirm":
        confirm(player)
    elif prompt == 'user':
        return user()

    return
