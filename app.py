import time
from database import add_entry, get_entries, close_connection

def prompt():
    date = input("Enter the date [dd-mm-yy]: ")
    content = input("What did you learn today?\n")
    add_entry(date, content)

def view():
    print("\n\nSTUDY JOURNAL\n----------------------------------------------------------\n")
    for entry in get_entries():
        print(entry[0], entry[1], sep="\n", end= "\n"*2)
    print("\n----------------------------------------------------------\n")

print("Welcome to Study Journal!\n")

#Store the strings for repeated use
menu = """\nPlease select one of the following options:
1 - Add new entry for today
2 - View entries
3 - Exit

Your selection: """

choice = int(input(menu))

while choice:
    if choice == 1:
        prompt()
    elif choice == 2:
        view()
    elif choice == 3:
        # I guess close_connection() can be added here instead.
        break
    else:
        print("Invalid choice. Please select one among 1, 2 and 3.")
    choice = int(input(menu))

print("\nClosing connection to database...")
time.sleep(2)
print("\nConnection closed.", "Bye-bye!", sep ="\n")
close_connection()
