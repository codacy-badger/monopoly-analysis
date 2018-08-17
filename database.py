# --- Module Import -----------------------------
import os
import sqlite3

import configuration
import service

"""
Database Module
---------------
This file is for connect, create, querry, update and reset database.


Do not use the database directly. Use 'transaction' instead. 
"""


def connect():
    """ Connect the database

    To connect the database, 'game.sqlite' file is required.
    You may need to create() the database first. 
    """

    # Open the database
    try:
        global DATABASE
        DATABASE = sqlite3.connect(configuration.CONFIG['database_path'])

        global DATABASE_CURSOR
        DATABASE_CURSOR = DATABASE.cursor()

    except Exception as inst:
        service.error(inst)


def initiate():
    """ Generate a new brand new table (database)

    Generally for starting the new game.
    """

    # Make sure the database is purged
    reset()

    # Open the database
    connect()

    database_path = configuration.CONFIG['database_path']

    if not os.path.exists(database_path):
        service.error("There is no game.sqlite in {}".format(database_path))

    create(configuration.CONFIG['database_create_file'])


def create(database_file_list: list):
    """ Create a database to the game.sql

    Args:
        database_file_list:
    """
    # Create database using pre-created CREATE script

    print(database_file_list)

    for j in database_file_list:

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

        except sqlite3.Error as inst:
            service.error("Problem raised from database.create() : " + str(inst))
            DATABASE.rollback()

        finally:
            DATABASE.close()


def describe(table_name):
    """ Describe the table attribute. Not for normal usage.

    Args:
        table_name:
    """
    connect()

    try:
        DATABASE.execute(
            "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = {}".format(table_name))
        DATABASE.commit()

    except sqlite3.Error as inst:
        service.error(inst)
        DATABASE.rollback()

    finally:
        DATABASE.close()


def select(column_name: str, table_name: str, ref_column_name: str = None, operator: str = None, quantity: str = None,
           fetch=False, limit: int = 999, top_amount=1.00, catch_exception=True):
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
        fetch:
        limit:
        top_amount:
        catch_exception:
    """

    # Open the database
    connect()

    try:
        where_script = "WHERE {} {} {}".format(ref_column_name, operator, quantity) \
            if ref_column_name is None or operator is None or quantity is None \
            else ""

        DATABASE.execute("SELECT {} FROM {} {} LIMIT {}".format(column_name, table_name, where_script, limit))

        return DATABASE_CURSOR.fetchall() if fetch else None

    except sqlite3.Error as inst:
        if not catch_exception:
            service.error("SQLite3 handle SELECT Query Error")

    finally:
        # Close the database
        DATABASE.close()


def update(table_name: str, column_name: str, column_quantity,
           ref_column: str, operator: str, ref_column_quantity):
    """ Do an UPDATE script on database

    UPDATE <table_name> 
    SET <column_name> = <column_quantity> 
    WHERE <ref_column> <operator> <ref_column_quantity>;

    Args:
        table_name:
        column_name:
        column_quantity:
        ref_column:
        operator:
        ref_column_quantity:
    """
    # Open the database
    connect()

    # Make transaction on UPDATE
    try:
        sql_script = "UPDATE {} SET {} {} {} WHERE {} = {};".format(
            table_name, column_name, operator, column_quantity, ref_column, ref_column_quantity)
        DATABASE.execute(sql_script)
        DATABASE.commit()

    except Exception as inst:
        DATABASE.rollback()
        service.error(inst)

    finally:
        # Close the database
        DATABASE.close()


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

    except Exception as inst:
        DATABASE.rollback()
        service.error(inst)

    finally:
        # Close the database
        DATABASE.close()


def exists(table_name: str, column_name: str, entry):
    # Open the database
    connect()

    result = False  # Set as default, if not changed by finally
    try:
        select(column_name, table_name, entry, catch_exception=False)
        result = True

    except sqlite3.OperationalError:
        service.warning("database.exists() create sqlite3.OperationalError")

    finally:
        # Return the database and return the result
        DATABASE.close()
        return result


def count(table_name: str):
    # Connect to the database
    connect()

    try:
        DATABASE.execute("SELECT COUNT(*) FROM {}".format(table_name))
        result = DATABASE_CURSOR.fetchall()
        return result

    except sqlite3.Error as inst:
        DATABASE.rollback()

        service.warning("Cannot count the result")
        service.warning(inst)

    finally:
        DATABASE.close()


def reset():
    """ Reset the database to make it newly generated

    NOTE: This function will be called during the game initiation.
    """
    service.log("Resetting the database")
    # Open the database
    connect()

    try:
        # Delete the old database file
        os.remove(configuration.CONFIG['database_path'])

        # Create the new database file
        file = open(configuration.CONFIG['database_path'], 'w+')
        file.close()

    except Exception as inst:
        service.error(inst)

    finally:
        service.log("Database has successfully purged")
