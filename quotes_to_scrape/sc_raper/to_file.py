import csv
import sqlite3


def to_csv_file(quotes: list):
    if quotes:
        # fields = ["Quotes", "Author", "About Author", "popular_tags", "link Popular"]
        fields = ["Quotes", "Author", "About Author"]

        with open('filename.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fields)
            for i in quotes:
                writer.writerow(i)
        return 'success', 200
    else:
        raise Exception("Quotes is empty")



def to_sqlite_file(quotes: list):
    try:
        sqliteConnection = sqlite3.connect('quotes.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO  quotes
                          (quotes, author, author_link, tags, tags_link) 
                          VALUES (?, ?, ?, ?, ?);"""

        cursor.executemany(sqlite_insert_query, quotes)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into SqliteDb_developers table")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def create_sqlite_file(filename: str):
    try:
        sqliteConnection = sqlite3.connect(f'{filename}.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        sqlite_create_table_query = '''CREATE TABLE quotes ("id" INTEGER NOT NULL UNIQUE,
         "quotes" TEXT NOT NULL, "author" text NOT NULL, "author_link"text NOT NULL,"tags"	text NOT NULL,
         "tagslink" text NOT NULL,PRIMARY KEY("id" AUTOINCREMENT));'''
        cursor.execute(sqlite_create_table_query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
