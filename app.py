from database import add_entry, view_entries, close_db, create_table

def menu():
    print("\nPlease select one of the following options:",
      "1 - Add new entry for today.","2 - View entries.",
      "3 - Exit.\n", sep= '\n')
    return int(input("Your selection: "))

def user_ip():
    entry = input("\nWhat did you learn today?\n")
    date = input("\nEnter the date[dd/mm/yyyy]: ")
    add_entry(entry, date)
    print("\nNew entry added!")

print("Welcome to programming diary!")
choice = menu()

while choice != 3:
    if choice == 1:
        user_ip()
        choice = menu()
    elif choice == 2:
        cur = view_entries()
        print(cur.fetchall())
        choice = menu()
    else:
        print("\nInvalid choice, Try again!")
        choice = menu()

close_db() 
print("\nSee you again!")
exit()

if __name__ == "__main__":
    main()
