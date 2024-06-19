#!/usr/bin/python3
""" all cities by state """

import sys
import MySQLdb


def list_cities_by_states(username, password, database, state_name):
    """ takes in the name of a state as an argument and lists all cities of that state """

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = conn.cursor()

    query = ("SELECT cities.id, cities.name FROM cities" 
             "JOIN states ON cities.state_id = states.id" 
             "WHERE states.name = %s ORDER BY cities.id ASC")

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    if rows:
        print(", ".join([row[1] for row in rows]))
    else:
        print()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities_by_states(sys.argv[1], sys.argv[2],\
            sys.argv[3], sys.argv[4])
