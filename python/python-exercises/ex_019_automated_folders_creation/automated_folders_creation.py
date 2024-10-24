import os
import shutil

# Loop through all the files in the current folder.
for filename in os.listdir('.'):
    # Filter Python files.
    if filename.endswith('.py'):
        # Extract the name of the file (which is the element beginning in the index 2 of the split).
        new_ex_name = '_'.join(filename.split('_')[2:])
        # Get the name without the extension.
        folder_name = os.path.splitext(filename)[0]
        # Create a new folder with the original numbered name of the file.
        os.makedirs(folder_name, exist_ok=True)
        # Rename the original file without the prefix, while moving to the new directory.
        new_filename = os.path.join(folder_name, new_ex_name)
        os.rename(filename, new_filename)
