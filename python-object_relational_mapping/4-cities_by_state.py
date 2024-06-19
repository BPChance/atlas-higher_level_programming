#!/usr/bin/python3
""" cities by states """

import sys
import MySQLdb


def list_all_cities(username, password, database):
    """ lists all cities from the database hbtn_0e_4_usa """

    conn = MySQLdb.connect(
        host="localhost",
        passwd=password,
        db=database,
        port=3306
    )

    cursor = conn.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities JOIN states ON cities.state_id = states.id")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

    if __name__ == "__main__":
        list_all_cities(sys.argv[1], sys.argv[2], sys.argv[3])