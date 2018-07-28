import os

import service

try:
    # SQLite is a infamous package. We need these.
    import sqlite3
except ImportError as inst:
    service.error(inst)
    # try:
    #     import pip
    #     pip.main(['install', sqlite3])


"""
This file is for connecting the database, update database, reset database.
Absolutely about doing something with database.

If doing the transaction preparation, use transaction module.
"""
DATABASE = None


def connect_database(db_src='config/StandardAmerican/property.db'):
    try:
        DATABASE = sqlite3.connect(db_src)
    except Exception as inst:
        service.error(inst)

    return


def generate_database():
    """
    Generate a new database from the script given in database folder.
    As these database cannot be reused.
    """
    for i in range(3):
        DATABASE.execute()

    # make sure the database change is commited.
    DATABASE.commit()
    pass


def find(column, table, row='Null', operator='=', quantity='Null'):
    """
    SELECT <column> FROM <table> WHERE <row> <operator> <quantity>
    """
    DATABASE.execute("SELECT {} FROM {} WHERE {} {} {}".format(
        column, table, row, operator, quantity))
    DATABASE.commit()
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
    DATABASE.execute("UPDATE {} SET {} {} {} WHERE {} = {}"
                     .format(table_name, column, operator, quantity, pk_column, pk_column_value))
