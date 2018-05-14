from sys import argv
script, filename = argv
current_file = open(filename)
print(current_file.read())
