import sqlite3

conn = sqlite3.connect("data.db")

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
    s = ""
    for i in journal:
        s += f"{i['date']}  {i['content']}\n"
    return s

