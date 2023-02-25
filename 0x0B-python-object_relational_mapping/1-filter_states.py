#!/usr/bin/python3
"""1-filter_states.py"""
import MySQLdb
import sys


if __name__ == "__main__":
    """1-filter_states.py"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    [print(state) for state in cur.fetchall() if state[1][0] == 'N']
    cur.close()
    db.close()
