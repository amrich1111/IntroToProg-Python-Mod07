# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrating Python's Pickling features and Structured
#               error handling features
# ChangeLog (Who,When,What):
# Aimee Richardson 2/28/23, Created script for assignment 07, Listing 9
# ---------------------------------------------------------------------------- #

# Import pickle module
import pickle

# Define the data
pickle_file = "moodTracker.abt"

# Functions
def output_menu_options():
   """  Display a menu of choices to the user

   :return: nothing
   """
   print('''
   Menu of Options
   1) Add New Entry (Remove Old Entries)
   2) Add New Entry (Keep Old Entries)
   3) View Current Entries 
   4) Exit Program
   ''')
   print()  # Add an extra line for looks


def input_menu_choice():
       """ Gets the menu choice from a user

       :return: string
       """
       choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
       print()  # Add an extra line for looks
       return choice


def add_entry():
   """  Gets user input and adds entry to pickled_list

          :return: nothing
          """
   user_date = str(input("Enter today's date: ")).strip()
   user_mood = str(input("Enter your mood: ")).strip().capitalize()
   while True:
       try:
           user_rate = int(input("Rate your day (1 - 10): "))
           break
       except ValueError: # If user doesn't enter a number, display message to user
           print("\nInvalid entry! Please only enter numbers.\n")
       except Exception as e:
           print(f"\nA {e.__class__.__name__} error has occurred!") # If any other error occurs, display error name to user
   pickled_list.append([user_date, user_mood, user_rate])  # Add user inputted data to list object
   print("\nEntry Added!")


def format_data():
   """  Formats and displays data from binary file to user

          :return: nothing
          """
   print("Current data:")
   print("Date | Mood | Daily Rating")
   for entry in unpickled_list:
       for item in entry:
           print(f"{item[0]}, {item[1]}, {item[2]}")


def write_new_data():
   """  Adds new entry data to binary file and overwrites existing data

          :return: nothing
          """
   add_entry()
   with open(pickle_file, "wb") as binary_file:  # Open/create new binary file to write new data to
       pickle.dump(pickled_list, binary_file)  # "Dump" data to binary file

def load_existing_data():
   """  Tries to read data from binary file and loads it into list object

          :return: nothing
          """
   try:
       with open(pickle_file, "rb") as binary_file:  # Open existing binary file to read data from
           while True:
               try: # Continue to read all objects file until all objects are loaded
                   unpickled_list.append(pickle.load(binary_file))  # "Load" data from binary
               except EOFError: # Once end of file is reached, break out of loop
                   break
       format_data()
   except FileNotFoundError: # If file not found, display message to user
       print("\nFile does not exist! Add data to the file to view.\n")
   except Exception as e:
       print(f"\nA {e.__class__.__name__} error has occurred!") # If any other error occurs, display error name to user

def append_data():
   """  Adds new entry and appends it to existing binary file

          :return: nothing
          """
   add_entry()
   with open(pickle_file, "ab") as binary_file: # Open/create a new or existing binary file to append new data to
       pickle.dump(pickled_list, binary_file) # "Dump" data to binary file


# Show user menu
print("Welcome to the Mood Tracker! Please select one of the following options:")
while True:
   # Define data
   pickled_list=[]
   unpickled_list=[]

   # Display menu
   output_menu_options()
   user_choice = input_menu_choice() # Stores user's menu selection

   # Write new data to binary file
   if user_choice == "1":
       write_new_data()
       continue
   # Add new data to existing file
   elif user_choice == "2":
       append_data()
       continue
   # Read data from binary file
   elif user_choice == '3':
       load_existing_data()
       continue
   # Exit program
   elif user_choice == '4':
       input("\nPress Enter to Exit")
       break
   else:
       print("Please only select 1 - 4!")
       continue