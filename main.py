<<<<<<< Updated upstream
=======
# --- Module Import -----------------------------
import service
import transaction
import database
import configuration
import actions
import startup

>>>>>>> Stashed changes
"""
Main Module
-----------
This module will initiate other module + start the game.

If you liked to start the program, type `python3 main.py`
"""

<<<<<<< Updated upstream
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
=======
# --- Check game file integrity ---------------------------
startup.check_core_file()
startup.check_database_file()
startup.check_game_file()

# --- Checking the library integrity ----------------------
startup.check_library()

# --- Start the service
service.announce("Initiating the service")
>>>>>>> Stashed changes

# -- Generate the database from the script ----------------
database.initiate()

<<<<<<< Updated upstream
# -- Add more players to the game until hitting ENTER -----
service.announce("Now I need player")
while True:
    try:
        actions.create_user()
    except:
        break
service.announce("Thanks!")
=======
# service.announce("Game package is loaded.")
# service.announce("Now I need player")

# -- Add more players to the game until hitting ENTER -----
# actions.create_user()
>>>>>>> Stashed changes

# Start the game process

# Roll the dice

# Action resolve

# Create actions

# Action resolve

# Repeat
