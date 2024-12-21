with open('Sample_File (1).txt', 'r') as file:
    contents = file.read()
    print(contents)
    file.write('This is a new content replacing old content.')
    file.write('\nThis line is appended to the file.')
