#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    sql_query = "SELECT * FROM states ORDER BY id;"
    cursor.execute(sql_query)
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
