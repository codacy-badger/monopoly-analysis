"""
Welcome to the configuration file, where you can set rules to the game...

Some game version package will have this file and it will overrides it.

Parameters:
    speed_dice (Default: False) -> Have speed dice in your game
    free_parking_skip_turn (Default: True) -> Skip player's 1 turn from moving
    money_unit (Default: M) -> The currency that will be used.
"""

CONFIG = {
    'game_package': '',
    'file_to_check': ['property.csv', 'game.sqlite', 'tiles.csv'],

    'auto_roll': False,
    'dice_face': {1, 2, 3, 4, 5, 6},
    'speed_dice': False,
    'speed_dice_face': {1, 2, 3, 'Mr. Monopoly', 'Mr. Monopoly', 'Bus'},
    'free_parking_skip_turn': True,
    'money_unit': 'M',
    'money_denomination': 1,

    'starter_money': 200,
    'pass_go_salary': 200,
    'income_tax': 200,
    'luxury_tax': 100,

    'jail_cost': 50,
    'auction_start_price': 0.1,
    'house_sell': 0.5,
    'remortgage_price': 0.6
}
