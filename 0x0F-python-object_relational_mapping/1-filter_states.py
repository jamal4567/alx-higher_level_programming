#!/usr/bin/python3
'''
 script that lists all states with a name,
 starting with N (upper N) from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

'''
Access to the database and get the states
from the database.
'''

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host = "localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    db = cur.fetchall()
    for i in db:
        print(i)