import os
import sys

import globalConfig
"""
Loader module will loads all the configuration files and information of the game.
If you liked to change the service information, please change it in config/global.config file.
"""


def configuration_loader():
    """
    """
    config = globalConfig.CONFIG


def get_money():
    return globalConfig.CONFIG['starter_money']
