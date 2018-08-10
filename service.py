# --- Module Import -----------------------------

"""
Service Module
--------------
Service gives information and asks prompt from user
"""


def error(instance: object):
    """ Send the users error issues. Program probably be stopped by the Exception.

    Args:
        instance:
    """
    print("{1}[ Error ]{2} > {0}".format(instance, '\x1b[6;30;41m', '\x1b[0m'))


def warning(instance: object):
    """ Send the users warning issues

    Args:
        instance:
    """
    print("{1}[ Warning ]{2} > {0}".format(
        instance, '\x1b[6;30;43m', '\x1b[0m'))


def log(log_text):
    """ Send the users log process

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
        Args:
            player:

        """
        print("{} > Are you sure?".format(player))
        result = bool(input())
        return result

    def user():
        """

        Returns:

        """
        announce("Please type in your player name. Press ENTER to stop")
        items = input()
        return items

    # Resolve the prompt here ----------
    if prompt == 'action':
        action(player)
    elif prompt == 'resolve':
        resolve(player)
    elif prompt == "confirm":
        confirm(player)
    elif prompt == 'user':
        return user()

    return
