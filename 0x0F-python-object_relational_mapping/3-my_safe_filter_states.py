#!/usr/bin/python3

# Import necessary modules
import sys
import MySQLdb

if __name__ == "__main__":
    """ Establish a connection to the MySQL database using provided credentials"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    """Create a cursor object to interact with the database"""
    c = db.cursor()

    """Execute an SQL query to select all rows from the 'states' table"""
    c.execute("SELECT * FROM `states`")

    """Fetch all rows from the query result and print those with a matching state name"""
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]

