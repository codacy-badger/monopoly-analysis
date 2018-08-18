"""
Database Module
---------------

This file is for connect, create, query, update and reset database.

Do not use the database directly. Use 'transaction' instead.
"""

import os
import sqlite3

import configuration
import service


def create(database_file_list: list):
    """ Create a database to the game.sql

    Args:
        database_file_list:
    """

    service.log("These file of SQL Script will be executed... " +
                str(database_file_list))

    for j in database_file_list:

        connect()
        service.log("Loading database file : {}".format(j))
        script = ""

        try:
            with open("config/database/{}".format(j)) as sql_script:
                for i in sql_script:
                    if i.find("--") == -1:
                        script += "{}\n".format(i)
                    else:
                        continue
                service.log(script)
                sql_script.close()  # Close file

            DATABASE.execute(script)
            DATABASE.commit()
            del script

        except sqlite3.Error as inst:
            service.error(
                "Problem raised from database.create() : " + str(inst))
            DATABASE.rollback()

        finally:
            DATABASE.close()


def connect():
    """ Connect the database

    To connect the database, 'game.sqlite' file is required.
    You HAVE to execute database.create() to create the database file first
    """

    # Open the database
    try:
        global DATABASE
        DATABASE = sqlite3.connect(configuration.CONFIG['database_path'])

        global DATABASE_CURSOR
        DATABASE_CURSOR = DATABASE.cursor()

    except Exception as inst:
        service.error(inst)


def disconnect():
    """ Disconnect the database

    After using the database, the connection should be closed.
    This code block will be optimized soon. Don't worry.
    """

    try:
        DATABASE.close()
        del DATABASE

        DATABASE_CURSOR.close()
        del DATABASE_CURSOR

    except sqlite3.Error as inst:
        service.error("Cannot close the database")


def initiate():
    """ Generate a new brand new table (database)

    Generally for starting the new game.
    """

    # Make sure the database is purged
    reset()

    # Open the database
    connect()

    # Create a database
    create(configuration.CONFIG['database_create_file'])


def describe(table_name):
    """ Describe the table attribute. Not for normal usage.

    Args:
        table_name:
    """
    connect()

    try:
        # DATABASE.execute(
        #     "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = {}".format(table_name))
        DATABASE.commit()

    except sqlite3.OperationalError as inst:
        service.error(inst)
        DATABASE.rollback()

    finally:
        disconnect()


def select(column_name: str, table_name: str, ref_column_name: str = None, operator: str = '=', quantity=None,
           limit: int = 999, top_percent: int = 100):
    """ Create a SELECT script on database

    Full SELECT script is :
    SELECT <column_name>
    FROM <table_name>
    WHERE <ref_column_name> <operator> <quantity>
    LIMIT <limit>

    If <ref_column_name> or <operator> or <quantity> is not given,
    WHERE statement will be removed.

    Args:
        column_name:
        table_name:
        ref_column_name:
        operator:
        quantity:
        limit:
        top_percent:
    """

    # Open the database
    connect()

    # Create a WHERE script
    if ref_column_name is None or operator is None or quantity is None:
        where_script = "WHERE {} {} {}".format(
            ref_column_name, operator, quantity)
    else:
        where_script = ""

    try:
        # Execute the SQL script
        DATABASE.execute(
            "SELECT {} {} FROM {} {} LIMIT {}".format(top_percent, column_name, table_name, where_script, limit))

        # Fetch the result from the query
        return DATABASE_CURSOR.fetchall()

    except sqlite3.OperationalError:
        service.error("SQLite3 handle SELECT Query Error")

    finally:
        disconnect()


def update(table_name: str, set_column_name: str, set_column_quantity,
           ref_column: str, ref_column_quantity, set_operator: str = '=', ref_operator='='):
    """ Do an UPDATE script on database

    UPDATE <table_name>
    SET <column_name> <set_operator> <column_quantity>
    WHERE <ref_column> <ref_operator> <ref_column_quantity>;

    Args:
        table_name:
        set_column_name:
        set_column_quantity:
        ref_column:
        ref_column_quantity:
        set_operator:
        ref_operator:
    """
    # Open the database
    connect()

    # Make transaction on UPDATE
    try:
        sql_script = "UPDATE {} SET {} {} {} WHERE {} {} {};".format(
            table_name, set_column_name, set_operator, set_column_quantity, ref_column, ref_operator,
            ref_column_quantity)

        DATABASE.execute(sql_script)
        DATABASE.commit()

    except sqlite3.OperationalError as inst:
        DATABASE.rollback()
        service.error(inst)

    finally:
        disconnect()


def insert(table_name: str, values: list):
    """ Do an INSERT script on database

    INSERT INTO <table_name> VALUES (<values>);

    Args:
        values:
        table_name:
    """
    # Open the database
    connect()

    # Change the values of list into a string
    values = str(values).lstrip('[').rstrip(']')

    # Execute a SQL command
    try:
        sql_script = "INSERT INTO {} VALUES ({})".format(table_name, values)
        DATABASE.execute(sql_script)
        DATABASE.commit()
        service.log("Execute SQL : {}".format(sql_script))

    except sqlite3.OperationalError as inst:
        DATABASE.rollback()
        service.error(inst)

    finally:
        disconnect()


def delete(table_name: str, ref_column_name: str, ref_values: str, operator: str = '='):
    """ Do a DELETE SQL Script

    Args:
        table_name:
        ref_column_name:
        operator:
        ref_values:
    """

    try:
        connect()

        DATABASE.execute("DELETE FROM {} WHERE {} {} {}".format(
            table_name, ref_column_name, operator, ref_values))

    except sqlite3.OperationalError as inst:
        service.error("Error on database.delete()")

    finally:
        disconnect()


def exists(column_name: str, table_name: str, quantity=None) -> bool:
    """ Check if there is a record in a certain table

    Args:
        column_name:
        table_name:
        quantity:

    Returns:

    """
    # Set as default, if not changed by finally
    result = False

    try:
        connect()

        # Do the SQL queries
        select(column_name=column_name, table_name=table_name, ref_column_name=column_name, quantity=quantity, limit=1)

        # If there is no errors on the prev. line, the result will return
        result = True

        # Actually returns the result
        return result

    except sqlite3.OperationalError:
        service.warning("database.exists() create sqlite3.OperationalError")

    finally:
        disconnect()


def count(table_name: str):
    """ Count the record from the table_name

    Args:
        table_name:

    Returns:

    """
    # Connect to the database

    try:
        connect()

        DATABASE.execute("SELECT COUNT(*) FROM {}".format(table_name))
        result = DATABASE_CURSOR.fetchall()
        return result

    except sqlite3.OperationalError as inst:
        DATABASE.rollback()

        service.warning("Cannot count the result")
        service.warning(inst)

    finally:
        disconnect()


def reset():
    """ Reset the database to make it newly generated

    NOTE: This function will be called during the game initiation.
    """

    try:
        service.log("Attempted to reset the database")

        # Delete the old database file
        os.remove(configuration.CONFIG['database_path'])

        # Create the new database file
        file = open(configuration.CONFIG['database_path'], 'w+')
        file.close()

    except BaseException as inst:
        service.error(inst)

    finally:
        service.log("Database has successfully purged")
