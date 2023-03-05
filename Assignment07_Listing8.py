# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrating Python's Pickling features and Structured
#               error handling features
# ChangeLog (Who,When,What):
# Aimee Richardson 2/28/23, Created script for assignment 07, Listing 8
# ---------------------------------------------------------------------------- #

# Import pickle module
import pickle

# Define data
pickle_file = "moodTracker.abt"
pickled_list = None
unpickled_list = []

# Present menu to user
print("Welcome to the Mood Tracker! Please select one of the following options:")
print('''
   Menu of Options
   1) Add New Entry (Remove Old Entries)
   2) Add New Entry (Keep Old Entries)
   3) View Current Entries 
   4) Exit Program
   ''')
print()  # Add an extra line for looks

# Get user input
user_choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()

# Write new data to binary file
if user_choice == "1":
   user_date = str(input("Enter today's date: ")).strip()
   user_mood = str(input("Enter your mood: ")).strip()
   while True:
      try:
         user_rate = int(input("Rate your day (1 - 10): "))
         break
      except ValueError: # If user doesn't enter a number, display message to user
         print("\nInvalid entry! Please only enter numbers.\n")
      except Exception as e:
         print(f"A {e.__class__.__name__} error has occurred!") # If any other error occurs, display error name to user
   pickled_list = [user_date, user_mood, user_rate]  # Add user inputted data to list object

   with open(pickle_file, "wb") as binary_file:  # Open/create new binary file to write new data to
       pickle.dump(pickled_list, binary_file)  # "Dump" data to binary file

   print("\nEntry Added!")

# Add new data to existing file
elif user_choice == "2":
   user_date = str(input("Enter today's date: ")).strip()
   user_mood = str(input("Enter your mood: ")).strip()
   while True:
      try:
         user_rate=int(input("Rate your day (1 - 10): "))
         break
      except ValueError: # If user doesn't enter a number, display message to user
         print("\nInvalid entry! Please only enter numbers.\n")
      except Exception as e:
         print(f"A {e.__class__.__name__} error has occurred!") # If any other error occurs, display error name to user
   pickled_list = [user_date, user_mood, user_rate]  # Add user inputted data to list object

   with open(pickle_file, "ab") as binary_file: # Open/create a new or existing binary file to append new data to
       pickle.dump(pickled_list, binary_file) # "Dump" data to binary file

   print("\nEntry Added!")

# Read data from binary file
elif user_choice == '3':
   try: # Try to read data from file
      with open(pickle_file, "rb") as binary_file:  # Open existing binary file to read data from
         while True: # Continue to load all objects file until all objects are loaded
            try:
               unpickled_list.append(pickle.load(binary_file))  # "Load" data from binary
            except EOFError:  # Once end of file is reached, break out of loop
               break
      print("\nCurrent Data:")
      print(unpickled_list)
   except FileNotFoundError: # If file not found, display message to user
      print("\nFile does not exist! Add new data to create a file.\n")
   except Exception as e: # If any other error occurs, display error name to user
      print(f"A {e.__class__.__name__} error has occurred!")

# Exit program
elif user_choice == '4':
   input("\nPress Enter to Exit")

input("\nPress Enter to Exit")
