import sqlite3 as sq

# Establishing a connection with the database:
conn = sq.connect("StudentJournalDB.db")
        # conn :- connection object
# context manager:
with conn:
    conn.execute("CREATE TABLE IF NOT EXISTS entries (date TEXT, content TEXT);")

def close_connection():
    conn.close()

def add_entry(date, content):
    """Function to add entries to the SQLite database
    """
    with conn:
        conn.execute("INSERT INTO entries VALUES(?, ?);", (date, content))
        # ip variables provided in tuples as second argument.
        # Do not use fstrings (Injection Attack!).
        # Use tuples to give input even if there is only one variable
            # Eg: (date,) -> single element tuple

def get_entries():
    """Function to retrieve entries from the SQLite database
    """
    return conn.execute("SELECT * FROM entries;")
