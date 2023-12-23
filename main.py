from mood_tracker_functions import add_entry, add_emotions, add_score, remove_entry, view_entries

file_name = "entries.csv"

try:
    #open the file in read mode
    entries_file = open(file_name, "r")
    entries_file.close
    print("In try block")
    #if it rhows error, it means the file doesn't exist
    #if no error, it mesns the file exists
except FileNotFoundError:
    #now we knhow the file doesnt exist
    #create the file
    entries_file = open(file_name, "w")
    #we can also insert the first line into the file
    entries_file.write("title,completed\n")
    entries_file.close()
    print("In except block")


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
        add_entry(file_name)
    elif (users_choice == "2"):
        remove_entry(file_name)
    elif(users_choice == "3"):
        add_score(file_name)
    elif (users_choice == "4"):
        add_emotions(file_name)
    elif(users_choice == "5"):
        view_entries(file_name)
    elif(users_choice == "6"):
        continue
    else:
        print("Invalid Inupt")

print("Thank you for using your mood tracker")