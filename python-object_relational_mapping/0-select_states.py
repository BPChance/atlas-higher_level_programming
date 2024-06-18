#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

def list_all_states(username, password, database):
    """connects to database and lists all states from the database hbtn_0e_0_us"""
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM states;")
    
    rows = cursor.fetchall()
    for row in rows:
          print(row)
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
        list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])