# Pickling & Error Handling in Python

## Introduction
In the following documentation we explore the pickling and exception handling features in Python. When handling binary files, the use of both pickling and exception handling together is important to ensure your program runs as intended. Pickling in Python allows programs to serialize and store complex objects to a file. In the following sections, we will walk through pickling and exception handling in Python while building a Mood Tracker. This program will allow users to input data to add new entries, access existing entries, and view all entries from a binary file.

## Binary vs. Text Files in Python
Python can handle loads of different variables and objects and save them to files. So far, we have become more familiar with working with text (.txt) files and saving user input to them. A limitation of text files is their inability to store complex objects such as entire lists or dictionaries. In order to save lists or dictionaries to text files you must iterate over them, and save individual parts of the larger object to the file. 

An alternative to using text files, which would require packing and unpacking lists into variables from text, is to store these complex objects in binary files. In order to effectively store data to binary files, an additional Python module needs to be utilized which will be explored further in the following section.

## Pickling in Python
The Pickle module in Python allows programmers to access multiple methods which facilitate the task of storing data in binary files. Pickle is a unique package that can be imported into any Python program when developers need to store complex objects to files. The following sections will go a bit more in depth regarding the pickle.dump() and pickle.load() methods and how those differ from how we might work with storing data in text files.

### Dumping with Pickle (Writing Data to a Binary File)
#### Listing 1
```
import pickle

# Define the data
pickle_file = "moodTracker.abt"
pickled_list = None

# Get user input
user_date = str(input("Enter today's date: ")).strip()
user_mood = str(input("Enter your mood: ")).strip()
user_rate = int(input("Rate your day (1 - 10): "))

# Process the data
pickled_list = [user_date, user_mood, user_rate] # Add user inputted data to list object

# Save data to file
binary_file = open(pickle_file, "wb") # Open/create new binary file to write new data to
pickle.dump(pickled_list, binary_file) # "Dump" data to binary 
binary_file.close() # Close file

# Presentation
print(f"Your data was saved!\n{pickled_list}\n")
input("Press Enter to Exit")
```


## Structured Error Handling in Python

## Utilizing Pickling & Error Handling Together

## Summary
