"""
Week13 Python Project1
"""

#!/usr/bin/env python3.7

# Import the Python os module, this will enable us use Operating System dependent functionality

import os

#Use os.getcwd() function to call the Current Working Directory (cwd)

working_directory = os.getcwd()

#Creating an empty list to store file information in a list of dictionaries.

empty_list = []

#Go through the directory tree and obtail the file details
for dirpath, dirnames, filenames in os.walk(working_directory ):
     for f in filenames:
        file_path = os.path.join(dirpath, f)
        file_size = os.path.getsize(file_path)
        empty_list.append({"name": f, "size": file_size})

# Print the list of dictionaries (using the 'sep' parameter with \n to separate each dictionary into a new line.)   

print(*empty_list, sep="\n")
