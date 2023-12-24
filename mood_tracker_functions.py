import csv


def add_entry(file_name):
    print("Add Entry")
    #Ask the titel of the entry
    entry_name = input("Add an entry title: ")
    #Insert value into file - entries.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([entry_name, "False"])
    #While inserting - title = what user entered
                  # - completed value = False

def remove_entry(file_name):
    print("Remove Entry")
    entry_name = input("Type the entry you would like to remove: ")
    entry_list = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (entry_name != row[0]):
                entry_list.append(row)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(entry_list)

import csv

def add_score(file_name):
    print("Rate day / 10")
    
    # Use input to get user input as a string
    user_input = input("Enter number between 0 and 10: ")
    
    try:
        # Convert the user input to an integer
        daily_rating = int(user_input)
        
        # Check if the entered integer is between 0 and 10
        if 0 <= daily_rating <= 10:
            with open(file_name, "a") as f:
                writer = csv.writer(f)
                writer.writerow([daily_rating, "False"])
        else:
            print("Invalid entry, please enter a number between 0 and 10")
    
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 10.")


def add_emotions(file_name):
    print("Add key emotions from the following list (case sensitive")
    emotions_list = ["Happy", "Sad", "Angry", "Content", "Grumpy"]

    while True:
        print("Choose an emotion from the following list (case sensitive):")
        print(emotions_list)
        chosen_emotion = input("Enter Selection: ")

        if chosen_emotion in emotions_list:
            with open(file_name, "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow([chosen_emotion, "False"])
            break  # Exit the loop if a valid emotion is entered
        else:
            print("Please choose from emotions above")

def mark_entry_complete(file_name):
    print("Mark entry complete")
    entry_name = input("Type entry that you would like to mark as complete: ")
    entry_list = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader: 
            if(entry_name != row[0]):
                entry_list.append(row)
            else:
                entry_list.append([row[0], "True"])
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(entry_list)

def view_entries(file_name):
    print("View all entries")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            if(row[1] == "True"):
                print(f"Entry {row[0]} is completed")
            else:
                print(f"Entry {row[0]} is not complete")

def complete_entry(file_name):
    print("Let's make a new entry!")
    
    entry_name = input("Add an entry title: ")

    print("Add key emotions")
    emotions_list = ["Happy", "Sad", "Angry", "Content", "Grumpy"]

    while True:
        print("Choose an emotion from the following list")
        print(emotions_list)
        chosen_emotion = input("Enter Selection: ")

        if chosen_emotion in emotions_list:
            break
        else:
            print("Please choose from emotions below (case sensitive)")

    print("Rate day / 10")
    
    while True:
        user_input = input("Enter number between 0 and 10: ")

        try:
            daily_rating = int(user_input)
            if 0 <= daily_rating <= 10:
                break
            else:
                print("Invalid entry, please enter a number between 0 and 10")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([entry_name, chosen_emotion, daily_rating, "False"])
