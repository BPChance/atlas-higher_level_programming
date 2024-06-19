#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb


def list_all_states(username, password, database):
    """ connects to the database and lists all states from the database hbtn_0e_0_usa """
    try:
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script_name.py username password database_name")
    else:
        list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
