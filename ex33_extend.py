print("1.String")
print("2.Number")
print("3.Both")
type = input("What kind of data type you enter:")
print(f"Weel.You choose the Type {type}.")
number = int(input("The line of the list is ? >"))
list = []

def make_list(number):
	i = 0
	while i < number:
		append = input(f"The {i+1} line is :")
		list.append(append)
		i += 1

make_list(number)
print(list)
