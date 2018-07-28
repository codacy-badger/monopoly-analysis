import os

import service
import configuration
import database

try:
    # SQLite is a infamous package. We need these.
    import sqlite3
except ImportError as inst:
    service.error(inst)


"""
This file is for connecting the database, update database, reset database.
Absolutely about doing something with database.

If doing the transaction preparation, use transaction module.
"""


def connect():
    # Open the database
    try:
        global DATABASE
        DATABASE = sqlite3.connect(configuration.CONFIG['database_path'])
    except Exception as inst:
        service.error(inst)
    return


def initiate():
    """
    Generate a new database from the script given in database folder.
    As these database cannot be reused.
    """
    database.connect()

    for _ in range(3):
        DATABASE.execute()

    # make sure the database change is commited + closed.
    DATABASE.commit()
    DATABASE.close()
    pass


def select(column, table, row='Null', operator='=', quantity='Null'):
    """
    SELECT <column> FROM <table> WHERE <row> <operator> <quantity>
    """
    database.connect()

    # Make transaction on SELECT
    DATABASE.execute("SELECT {} FROM {} WHERE {} {} {}".format(
        column, table, row, operator, quantity))

    # make sure the database change is commited + closed.
    DATABASE.commit()
    DATABASE.close()
    pass


def update(table_name, column, operator, quantity, pk_column, pk_column_value):
    """
    Do this transaction (IN SQL)
    UPDATE <table_name> SET <column> <operator> <quantity> WHERE <pk_column> = <pk_column_value>

    :param column:
    :param table:
    :param row:
    :param quantity:
    :return:
    """
    # Open the database
    database.connect()

    # Make transaction on UPDATE
    DATABASE.execute("UPDATE {} SET {} {} {} WHERE {} = {}"
                     .format(table_name, column, operator, quantity, pk_column, pk_column_value))

    # make sure the database change is commited + closed.
    DATABASE.commit()
    DATABASE.close()


def insert(table_name, pk_column):
    # Open the database
    database.connect()

    # Give the default value for new entries, but need to check data

    # DATABASE.execute("INSERT INTO {} VALUES {}", table_name, query_string)


def reset_database():
    """
    WARNING: This function is destructive.
    Only used during the reset of the game.
    """
    database.connect()
    pass
