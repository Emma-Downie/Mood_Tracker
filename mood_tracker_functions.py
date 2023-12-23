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

def add_score(file_name):
    print("Rate day / 10")

def add_emotions(file_name):
    print("Add key emotions")

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
