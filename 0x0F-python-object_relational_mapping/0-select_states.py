#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    host = "localhost"
    user = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host, user, password, database)
    cursor = db.cursor()

    sql_query = "SELECT * FROM states ORDER BY id"
    cursor.execute(sql_query)
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()

