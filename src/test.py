
# Open a file for writing (creates the file if it doesn't exist)
with open('output.txt', 'w') as file:
    # Write text to the file
    file.write('This is a simple text file.\n')
    file.write('You can write multiple lines like this.\n')
    file.write('And close the file when you are done.\n')

print('Text file "output.txt" has been created and written to.')
