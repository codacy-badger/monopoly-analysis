import os

import configuration
import service

"""
Support Module
--------------
This module will check the game file configurations
and do data integrity check
"""


def check_game_file():
    """ Use for checking the game package configuration.

    Raises:
        IOError : File cannot be found in a correct folder
    """

    game_package = configuration.CONFIG['game_package']

    if not os.path.isdir("config/{}".format(game_package)):
        service.error("Path does not exists!")
        raise IOError

    for i in configuration.CONFIG['file_to_check']:
        if not os.path.exists("config/{}/{}".format(game_package, i)):
            service.error(
                "{} does not exists in game package folder. Creating new one.".format(i))
            file = open("config/{}/{}".format(game_package, i), 'w+')
            file.close()

    return


def check_database_file():
    """

    """
    def create_database_file():
        """

        """
        pass

    pass


def check_core_file():
    """

    """
    pass


def check_library():
    """

    """
    pass
