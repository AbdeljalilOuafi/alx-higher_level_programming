#!/usr/bin/python3

"""Get all states starting with 'N' and display them."""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id ORDER BY cities.id;"
        )
    result = cursor.fetchall()

    for tuple in result:
        print(tuple)

    cursor.close()
    db.close()
