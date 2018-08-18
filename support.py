"""
Support Module
--------------

This module will check the game file configurations
and do data integrity check
"""

import os

import configuration
import service


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
            service.warning(
                "{} does not exists in game package folder. Creating new one.".format(i))
            file = open("config/{}/{}".format(game_package, i), 'w+')
            file.close()


def check_database_file():
    """ Check if the database file is still in the folder

    """
    database_path = configuration.CONFIG['database_path']

    if not os.path.exists(database_path):
        service.error("There is no game.sqlite in {}".format(database_path))
