from sys import argv
script, filename = argv
write_file = open(filename,'w')
line_count = eval(input("how many line ? "))
for i in range (line_count):
	data = input(f"Input the {i+1} line:")
	write_file.write(data)
	write_file.write("\n")
write_file.close()
write_file =open(filename)
print(write_file.read())
