journal = []

def add_entry():
    entry = input("\nWhat have you learned today?\n")
    date = input("Enter the date(dd/mm/yyyy): ")
    journal.append({"content":entry, "date":date})

def view_entries():
    print("\nDisplaying...\n")
    for i in journal:
        print(f"{i['date']}  {i['content']}")
