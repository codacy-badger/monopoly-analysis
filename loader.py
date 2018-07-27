import os
import sys

import globalConfig
"""
Loader module will loads all the configuration files and information of the game.
If you liked to change the service information, please change it in config/global.config file.
"""

try:
    os.path.exists(GLOBAL_CONFIG_PATH)
except Exception:
    raise IOException

def configuration_loader():
    """
    """


def get_money():
    pass
