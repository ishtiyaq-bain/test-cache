import os

file_path = os.environ.get('RUN_ID')

with open(file_path, 'w') as file:
    file.write('This is a simple text file.\n')
    file.write('You can write multiple lines like this.\n')
    file.write('And close the file when you are done.\n')

print(f"Text file {file_path} has been created and written to.")
