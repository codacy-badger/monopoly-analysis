"""
Main Module
-----------
This module will initiate other module + start the game.

If you liked to start the program, type `python3 main.py`
"""

import support
support.check_library()
support.check_game_package_configuration()
support.check_module()

# --- Module Import ---------------------------------------
import service
import transaction
import database
import configuration
import actions

# --- Starting the program initiation --------------------
service.announce("Initiating the service")
service.prompt(prompt='package')
service.announce("Game package is loaded.")

# -- Generate the database from the script ----------------
database.initiate()

# -- Add more players to the game until hitting ENTER -----
service.announce("Now I need player")
while True:
    try:
        actions.create_user()
    except:
        break
service.announce("Thanks!")

# Start the game process

# Roll the dice

# Action resolve

# Create actions

# Action resolve

# Repeat
