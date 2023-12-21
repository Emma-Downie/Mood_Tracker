print("Welcome to your Mood Tracker")

def create_menu():
    print("1. Enter 1 to add a diary entry")
    print("2. Enter 2 to remove a diary entry")
    print("3. Enter 3 to add a score/10 for the day")
    print("4. Enter 4 to add key emotion words for the day")
    print("5. Enter 5 to view all entries")
    print("6. Enter 6 to exit")
    choice = input("Enter your selection: ")
    return choice

users_choice = ""

while users_choice != "6":
    users_choice = create_menu()
    if (users_choice == "1"):
        print("You entered 1")
    elif (users_choice == "2"):
        print("You enetered 2")
    elif(users_choice == "3"):
        print("You entered 3")
    elif (users_choice == "4"):
        print("You enetered 4")
    elif(users_choice == "5"):
        print("You entered 5")
    elif(users_choice == "6"):
        continue
    else:
        print("Invalid Inupt")

print("Thank you for your entry")