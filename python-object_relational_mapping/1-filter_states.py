#!/usr/bin/python3
""" lists all states with a name starting with N """

import sys
import MySQLdb

def list_states_with_n(username, password, database):
    """ connectcs to database and lists all states with a name starting with 'N' """

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states_with_n(sys.argv[1], sys.argv[2], sys.argv[3])
