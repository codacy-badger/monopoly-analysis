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
    print("{1}[ Error ]{2} {0}".format(instance, '\x1b[6;30;41m', '\x1b[0m'))


def warning(instance: object):
    """ Send the users warning issues

    Args:
        instance:
    """
    print("{1}[ Warning ]{2} {0}".format(
        instance, '\x1b[6;30;43m', '\x1b[0m'))


def log(log_text):
    """ Send the users log process

    Args:
        log_text:
    """
    print('\x1b[6;30;42m' + "[ Log ]" + '\x1b[0m' + " ", end="")
    print(log_text)


def announce(text: str):
    """ This function is used to format the program.

    Args:
        text: (String) the text that will be shown.
    """
    print("\nService {}".format(text))

    return


def prompt(player=None, prompted_text=None):
    """ Prompt user to do something to resolve background requests

    Args:
        prompted_text (String): Custom text that other function wants to show to user
        player (String): Username of the player that needs to resolve request
    """

    def action(username: str):
        """ Give user information on how to resolve the turn actions

        Args:
            username:
        """
        print("{} > Please choose action(s)".format(username))
        print("{}\t{}\t{}".format(
            '[ /roll ] Roll a dice',
            '[ /upgrade ] Buy house/hotel on a property',
            '[ /auto ] Automatically make a decision'))

    def resolve(username: str):
        """ Give user information on how to resolve the unowned property

        Args:
            username (str):
        """
        print("{} > Please choose action(s)".format(username))
        print("{}\t{}\t{}]\t{}\t{}".format(
            '[ /buy ] Buy Property at full price',
            '[ /auction ] Auction this property',
            '[ /trade ] Trade money or Property',
            '[ /done ] Finished your turn',
            '[ /auto ] Automatically make a decision'))

    def confirm(username: str) -> bool:
        """ Prompt user to confirm the transaction
        Args:
            username (str):

        """
        print("{} > Are you sure?".format(username))
        result = bool(input())
        return result

    def user() -> str:
        """ Prompt user with username input

        Returns:
            items (str):

        """
        announce("Please type in your player name. Press ENTER to stop")
        items = input()
        return items

    # Resolve the prompt here ----------
    if prompted_text == 'action':
        action(player)
    elif prompted_text == 'resolve':
        resolve(player)
    elif prompted_text == "confirm":
        confirm(player)
    elif prompted_text == 'user':
        return user()
