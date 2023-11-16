from database import add_entry, view_entries

def menu():
    print("\nPlease select one of the following options:",
      "1 - Add new entry for today.","2 - View entries.",
      "3 - Exit.\n", sep= '\n')
    return int(input("Your selection: "))

print("Welcome to programming diary!")
choice = menu()

while choice != 3:
    if choice == 1:
        add_entry()
        print("\nNew entry added!")
        choice = menu()
    elif choice == 2:
        view_entries()
        choice = menu()
    else:
        print("\nInvalid choice, Try again!")
        choice = menu()
        
print("\nSee you again!")
exit()

if __name__ == "__main__":
    main()
