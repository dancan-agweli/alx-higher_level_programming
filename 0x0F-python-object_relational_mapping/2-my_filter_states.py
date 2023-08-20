#!/usr/bin/python3
""" script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"
    cur.execute(query, (argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)

