import service
import transaction
import database
import configuration

service.announce("Initiating the service")
service.prompt(prompt='package')

# -- Generate the database from the script ----------------
# database.initiate()

service.announce("Game package is loaded.")
service.announce("Now I need player")

# -- Add more players to the game until hitting ENTER -----
while True:
    try:
        service.create_user()
    except:
        break
service.announce("Thanks!")
