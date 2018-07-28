import service
import transaction
import database
import configuration


def start():
    """
    This fucntion will basically a program starter.
    Probably doing everything...

    Parameters:
        none

    Return:
        none

    Raise:
        RunTimeException

    """
    service.announce("Initiating the service")
    service.user_prompt(prompt='package')

    # Generate the database from the script
    # loader.generateDatabase()

    service.announce("Game package is loaded.")
    service.announce("Now I need player")

    # Add more players to the game until hitting ENTER
    try:
        service.user_prompt(prompt='username')
    except EOFError:
        service.announce("Thanks. ")


# class Player:
#     def __init__(self):
#         self.money = loader.getMoney()
#         self.property = dict()


start()
