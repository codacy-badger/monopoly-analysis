""" Main Module

This module will initiate other module + start the game.

If you liked to start the program, type `python3 main.py`
"""

import actions
import database
import service
import support

try:
    # --- Starting the program initiation ---------------------
    service.announce("Initiating the service")

    # --- Check game file integrity ---------------------------
    support.check_database_file()
    support.check_game_file()

    # -- Generate the database from the script ----------------
    database.initiate()

    # -- Add more players to the game until hitting ENTER -----
    actions.create_user()

    # -- Preparing the game process -------------------------------
    actions.generate_game()

    # -- Start the game
    global CURRENT_PLAYER
    
    while True:
        try:
            pass
            # Roll the dice
            # Action resolve
            # Create actions
            # Action resolve
            # Repeat

        except KeyboardInterrupt:
            # Stop the game, because user is stopping the instance
            break
    
except KeyboardInterrupt:
    service.log("Stopped by KeyboardInterrupt")

finally:
    # Make sure that the database is disconnected before the program stops
    database.disconnect()
