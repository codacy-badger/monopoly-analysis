"""
This module store set of game rules.
For advanced player, you can edit this file to suit your game experience

Parameters:
    speed_dice (Default: False) -> Have speed dice in your game
    free_parking_skip_turn (Default: True) -> Skip player's 1 turn from moving
    money_unit (Default: M) -> The currency that will be used.
"""

CONFIG = {
    'game_package': 'StandardAmerican',
    'file_to_check': ['property.csv', 'game.sqlite', 'tiles.csv'],

    'database_path': 'config/StandardAmerican/game.sqlite',
    'database_create_path': 'config/database/',
    'database_create_file': ['Player.sql', 'PlayerProperty.sql', 'Property.sql'],

    'auto_roll': False,
    'dice_face': (1, 2, 3, 4, 5, 6),
    'dice_count': 2,

    'speed_dice': False,
    'speed_dice_face': (1, 2, 3, 'Mr. Monopoly', 'Mr. Monopoly', 'Bus'),

    'free_parking_skip_turn': True,
    'money_unit': '$',
    'money_denomination': 1,

    'starter_money': 200,
    'pass_go_salary': 200,

    'income_tax': 200,
    'luxury_tax': 100,

    'jail_cost': 50,
    'free_jail_double_roll': True,
    'free_jail_double_roll_attempt': 2,

    'three_double_jail': True,

    'auction_start_price': 0.1,
    'auction_start_price_mode': 'relative',

    'house_sell': 0.5,
    'house_sell_mode': 'relative',

    'remortgage_price': 0.6,
    'remortgage_price_mode': 'relative'
}

def update(key: str, value):
    """
    Use for updating the configuration dictionary

    Parameter:
        key: setting topic that want to be changed
        value: new value to be changed into
    """
    if value is not None:
        service.announce("Overriding '{}' from configuration".format(key))
        configuration.CONFIG[key] = value

    return
