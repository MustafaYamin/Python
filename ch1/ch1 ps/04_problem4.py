import os

# Select the directory you want the content of
directory_path = '/'

# Get the list of all files and directories in the root directory
entries = os.listdir(directory_path)

# Iterate over the list of entries
for entry in entries:
    print(entry)
