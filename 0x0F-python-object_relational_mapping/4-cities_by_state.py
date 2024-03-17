#!/usr/bin/python3
"""
script that lists all cities
from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    con = MySQLdb.connect(
            host='localhost', port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])
    cur = con.cursor()
    cur.execute(
            "SELECT cities.id, cities.name, states.name FROM \
                cities INNER JOIN states ON states.id=cities.state_id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
