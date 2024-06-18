#!/usr/bin/python3
import sys
import MySQLdb

def list_all_states(username, password, database):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])