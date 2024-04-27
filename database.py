db = []

def add_entry(date, content):
    """Function to add entries to the database
    """
    db.append({"date":date, "content":content})

def get_entries():
    return db
