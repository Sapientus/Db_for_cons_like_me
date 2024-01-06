import sqlite3  # Of course, I could do it eith postgres but I want to try this method too. So lets play with sql :)


def create_db():
    with open("school.sql", "r") as f:  # read db file
        sql = f.read()

    with sqlite3.connect("school.db") as con:  # create connection and db
        cur = con.cursor()  # our cursor for operations
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()
