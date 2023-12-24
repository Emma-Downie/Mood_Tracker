from colored import fg, attr, bg
from mood_tracker_functions import add_entry, add_emotions, add_score, remove_entry, view_entries, mark_entry_complete, complete_entry

file_name = "entries.csv"

try:
    #open the file in read mode
    entries_file = open(file_name, "r")
    entries_file.close
    # print("In try block") commented out as didn't like the addition

except FileNotFoundError:
    entries_file = open(file_name, "w")
    entries_file.write("title,completed\n")
    entries_file.close()
    # print("In except block") commented out as didnt like the addition


print(f"{fg('magenta')}{bg('white')}Welcome to your Mood Tracker{attr('reset')}")

complete_entry(file_name)



def create_menu():
    print("1. Enter 1 to view all entries")
    print("2. Enter 2 to mark entry complete")
    print("3. Enter 3 to add another entry")
    print("4. Enter 4 to exit")
    choice = input("Enter your selection: ")
    return choice

users_choice = ""

while users_choice != "4":
    users_choice = create_menu()
    if(users_choice == "1"):
        view_entries(file_name)
    elif(users_choice == "2"):
        mark_entry_complete(file_name)
    elif(users_choice == "3"):
        complete_entry(file_name)
    elif(users_choice == "4"):
        continue
    else:
        print("Invalid Inupt")

print(f"{fg('magenta')}{bg('white')}Thank you for using your mood tracker{attr('reset')}")