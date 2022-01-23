# Try to open a file that doesn't exist - to raise an exception ;-)
with open("a_file.txt") as file:
    file.read()
    
