"""
Week13 Python Project
"""

#!/usr/bin/env python3.7
import os

working_directory = os.getcwd()

empty_list = []

for dirpath, dirnames, filenames in os.walk(working_directory ):
     for f in filenames:
        file_path = os.path.join(dirpath, f)
        file_size = os.path.getsize(file_path)
        empty_list.append({"name": f, "size": file_size})
   
print(*empty_list, sep="\n")








