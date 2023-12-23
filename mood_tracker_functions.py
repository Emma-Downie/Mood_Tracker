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

def add_score(file_name):
    print("Rate day / 10")

def add_emotions(file_name):
    print("Add key emotions")

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
