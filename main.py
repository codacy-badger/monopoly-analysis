import service
import loader
import database


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
    service.announce(
        "Welcome to Monopoly Analysis. Please choose the game package.")
    loader.configuration_loader()


# class Player:
#     def __init__(self):
#         self.money = loader.getMoney()
#         self.property = dict()


start()
