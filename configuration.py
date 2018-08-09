"""
This module store set of game rules.
For advanced player, you can edit this file to suit your game experience

To see how to edit this file, please checkout our wiki here : https://github.com/sagelga/monopoly-analysis/wiki/Configurations
"""

CONFIG = {
    'game_package': 'StandardAmerican',
    'file_to_check': ['property.csv', 'game.sqlite', 'tiles.csv'],

    'database_path': 'config/StandardAmerican/game.sqlite',
    'database_create_path': 'config/database/',
    'database_create_file': ['Player.sql', 'Property.sql', 'PlayerProperty.sql', 'MoneyTransaction.sql',
                             'RollTransaction.sql'],

    'auto_roll': False,
    'dice_face': (1, 2, 3, 4, 5, 6),
    'dice_count': 2,

    'speed_dice': False,
    'speed_dice_face': (1, 2, 3, 'Mr. Monopoly', 'Mr. Monopoly', 'Bus'),

    'free_parking_skip_turn': True,
    'money_unit': '$',
    'money_unit_location': 'left',
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
    'remortgage_price_mode': 'relative',

    'liquidate_weight': {'mortgage': 1, 'sell': 0.5, 'sell_when_monopoly': 0.1, 'dice_probability': 0.5}
}


def add(key: str, value: object):
    """ Add a temporary configuration into dictionary

    Args:
        key:
        value:
    """
    if key is not None and value is not None:
        CONFIG[key] = value


def update(key: str, value):
    """ Use for updating the configuration dictionary

    Args:
        key: setting topic that want to be changed
        value: new value to be changed into
    """
    import service

    if key is not None and value is not None:
        service.log("Overriding '{}' from configuration".format(key))
        CONFIG[key] = value

    return
