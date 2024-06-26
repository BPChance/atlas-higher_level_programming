#!/usr/bin/python3
""" SQL Injection... """
import sys
import MySQLdb


def search_states_by_name(username, password, database, state_name):
    """
    Connects to a MySQL database and searches for states with a given name
    from the 'states' table sorted by 'id' in ascending order. 
    """
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC".format(state_name)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        search_states_by_name(username, password, database, state_name)
