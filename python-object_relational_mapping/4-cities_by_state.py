#!/usr/bin/python3
""" script that lists all cities"""

import MySQLdb
import sys


def list_cities(usr, pw, db_name):
    """ List all cities from the database. """

    db = MySQLdb.connect(host="localhost",
                         user=usr,
                         passwd=pw,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states ON cities.state_id = states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
