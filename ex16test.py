from sys import argv
script, filename = argv
print(f"Now we are raeding {filename}")
txt = open(filename)
print(txt.read())
