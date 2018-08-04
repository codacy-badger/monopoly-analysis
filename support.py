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
                "{} does not exists in game package folder!".format(i))
            raise IOError

    return


def check_library():
    """ Check library that are required in each module.
    """
    try:
        # --- Module Import -----------------------------
        import service
        import transaction
        import database
        import configuration
        import actions
        import support

        # --- External Module Import
        import sqlite3

    except Exception as inst:
        print("Unable to load some core module")


def check_database_file():
    def create_database_file():
        pass

    pass


def check_core_file():
    pass
