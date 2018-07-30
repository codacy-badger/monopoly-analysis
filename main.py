# --- Module Import -----------------------------
import service
import transaction
import database
import configuration
import actions

"""
This module will initiate other module + start the game.
If you liked to start the program, type `python3 main.py`
"""

service.announce("Initiating the service")
service.prompt(prompt='package')

# -- Generate the database from the script ----------------
database.initiate()

service.announce("Game package is loaded.")
service.announce("Now I need player")

# -- Add more players to the game until hitting ENTER -----
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
