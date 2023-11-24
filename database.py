import sqlite3

conn = sqlite3.connect("data.db")
#conn.row_factory = sqlite3.Row

def create_table():
    with conn:
        conn.execute("CREATE TABLE diary(content TEXT, date TEXT);")

def close_db():
    conn.close()

journal = []

def add_entry(entry, date):
    #journal.append({"content":entry, "date":date})
    with conn:
        conn.execute("INSERT INTO diary VALUES(?, ?)", (entry, date))

def view_entries():
    return conn.execute("SELECT * FROM diary;")
