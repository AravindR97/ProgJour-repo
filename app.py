from database import add_entry, get_entries

def prompt():
    date = input("Enter the date [dd-mm-yy]: ")
    content = input("What did you learn today?\n")
    add_entry(date, content)

def view():
    print("\n\nSTUDY JOURNAL\n----------------------------------------------------------\n")
    for entry in get_entries():
        print(entry["date"], entry["content"], sep="\n")
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
        print("\nBye-bye!")
        break
    else:
        print("Invalid choice. Please select one among 1, 2 and 3.")
    choice = int(input(menu))
