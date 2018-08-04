"""
Main Module
-----------
This module will initiate other module + start the game.

If you liked to start the program, type `python3 main.py`
"""

# --- Load library ----------------------------------------
import actions
import database
import service
import support

support.check_core_file()
support.check_database_file()
support.check_game_file()

# --- Starting the program initiation ---------------------
service.announce("Initiating the service")

# --- Check game file integrity ---------------------------
support.check_core_file()
support.check_database_file()
support.check_game_file()

# --- Checking the library integrity ----------------------
support.check_library()

# -- Generate the database from the script ----------------
database.initiate()

# -- Add more players to the game until hitting ENTER -----
actions.create_user()

# Start the game process

# Roll the dice

# Action resolve

# Create actions

# Action resolve

# Repeat
