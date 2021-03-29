#!/usr/bin/python3


def connectToDB():
    db = MySQLdb.connect(host=localhost,
                         user=sys.argv(1),
                         passwd=sys.argv(2),
                         port=3306,
                         db=sys.argv(3))

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
if __name__ == '__main__':
    import MySQLdb
    import sys
    connectToDB()
