import os

import actions
import configuration
import database
# --- Module Import -----------------------------
import service

try:
    # SQLite is a infamous package. We need these.
    import sqlite3
except ImportError as inst:
    service.error(inst)

"""
Database Module
---------------
This file is for connecting the database, update database, reset database.
100% about doing any transaction with database.

If you want to create a transaction that created from action, use Transaction module
"""


def connect():
    """ Connect the database

    Using the SQLite, the database is stored locally.

    Args:
        none

    Returns:
        none

    Raises:
        IOError :
    """
    # Open the database
    try:
        global DATABASE, DATABASE_CURSOR

        DATABASE = sqlite3.connect(configuration.CONFIG['database_path'])
        DATABASE_CURSOR = DATABASE.cursor()
    except Exception as inst:
        service.error(inst)
    return


def initiate():
    """ Generate a new brand new table (database)

    Generally for starting the new game.

    Args:
        none

    Returns:
        none

    Raises:
        IOError :
    """
    # Make sure that the old ones is deleted properly
    database.reset()

    # Connect the database
    database.connect()

    # Check for old database file
    if not os.path.exists(configuration.CONFIG['database_path']):
        service.error("There is no game.sqlite in {}".format(
            configuration.CONFIG['database_path']))

    # Create database using pre-created CREATE script
    for j in configuration.CONFIG['database_create_file']:
        service.log(j)
        script = ""

        with open("config/database/{}".format(j)) as sql_script:
            for i in sql_script:
                script += "{}\n".format(i)
            # logging.debug(script)
            sql_script.close()  # Close file

        DATABASE.execute(script)

    # make sure the database change is closed.
    DATABASE.commit()
    DATABASE.close()
    pass


def select(column, table, row='Null', operator='=', quantity='Null'):
    """ Create a SELECT script on database

    SELECT <column> FROM <table> WHERE <row> <operator> <quantity>

    Args:
        column :
        table :
        row :
        operator :
        quantity :

    Returns:
        none

    Raises:
        none
    """
    database.connect()

    # Make transaction on SELECT
    DATABASE.execute("SELECT {} FROM {} WHERE {} {} {};".format(
        column, table, row, operator, quantity))

    # make sure the database change is commited + closed.
    DATABASE.commit()
    DATABASE.close()
    pass


def update(table_name, column, operator, column_quantity,
           where_column, where_column_value):
    """ Do an UPDATE script on database

    UPDATE <table_name> SET <column> <operator> <column_quantity> WHERE <where_column> = <where_column_value>

    Args:
        table_name :
        column :
        operator :
        column_quantity :
        where_column :
        where_column_value :

    Return:
        none

    Raise:
        none
    """
    # Open the database
    database.connect()

    # Make transaction on UPDATE
    try:
        DATABASE.execute("UPDATE {} SET {} {} {} WHERE {} = {};"
                         .format(table_name, column, operator, column_quantity,
                                 where_column, where_column_value))

        # make sure the database change is committed + closed.
        DATABASE.commit()
        DATABASE.close()
    except Exception as inst:
        DATABASE.rollback()
        service.error(inst)


def insert(table_name: str, values: list):
    """ Do an INSERT script on database

    INSERT INTO <table_name> VALUES (<values>);

    Args:
        values:
        table_name:

    Return:
        none

    Raise:
        none
    """
    # Open the database
    database.connect()

    # Give the default value for new entries, but need to check data

    # Execute a SQL command
    try:
        DATABASE.execute("INSERT INTO {} VALUES ({})"
                         .format(table_name, values))
        DATABASE.commit()
        DATABASE.close()
    except Exception as inst:
        DATABASE.rollback()
        service.error(inst)

    pass


def reset():
    """ Reset the database to make it newly generated

    NOTE: This function will be called during the game initiation.

    Args:
        none

    Return:
        none

    Raise:
        none
    """
    service.log("Resetting the database")
    # Open the database
    database.connect()

    try:
        # Delete the old database file
        os.remove(configuration.CONFIG['database_path'])

        # Create the new database file
        file = open(configuration.CONFIG['database_path'], 'w+')
        file.close()

    except Exception as inst:
        # Rollback the change
        service.error(inst)
    pass
