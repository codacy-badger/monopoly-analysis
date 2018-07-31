import os
import logging

# --- Module Import -----------------------------
import service
import configuration
import database

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
        global DATABASE
        DATABASE = sqlite3.connect(configuration.CONFIG['database_path'])
        DATABASE = DATABASE.cursor()
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
    # Connect the database
    database.connect()

    # Check for old database file
    if not os.path.exists(configuration.CONFIG['database_path']):
        service.error("There is no game.sqlite in {}".format(
            configuration.CONFIG['database_path']))

    # Create database using pre-created CREATE script
    for j in configuration.CONFIG['database_create_file']:
        script = ""
        with open("config/database/{}".format(j)) as sql_script:
            for i in sql_script:
                script += "{}\n".format(i)
            # logging.debug(script)
            sql_script.close()  # Close file

        DATABASE.execute(script)

    # make sure the database change is closed.
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
    DATABASE.execute("SELECT {} FROM {} WHERE {} {} {}".format(
        column, table, row, operator, quantity))

    # make sure the database change is commited + closed.
    DATABASE.commit()
    DATABASE.close()
    pass


def update(table_name, column, operator, quantity, pk_column, pk_column_value):
    """ Do an UPDATE script on database

    UPDATE <table_name> SET <column> <operator> <quantity> WHERE <pk_column> = <pk_column_value>

    Args:
        table_name :
        column :
        operator :
        quantity :
        pk_column :
        pk_column_value :

    Return:
        none

    Raise:
        none
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
    """ Do an UPDATE script on database

    UPDATE <table_name> SET <column> <operator> <quantity> WHERE <pk_column> = <pk_column_value>

    Args:
        none

    Return:
        none

    Raise:
        none
    """
    # Open the database
    database.connect()

    # Give the default value for new entries, but need to check data

    # DATABASE.execute("INSERT INTO {} VALUES {}", table_name, query_string)
    pass


def reset_database():
    """ Do an UPDATE script on database

    UPDATE <table_name> SET <column> <operator> <quantity> WHERE <pk_column> = <pk_column_value>

    Args:
        none

    Return:
        none

    Raise:
        none
    """
    database.connect()
    pass
