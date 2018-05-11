def print_two(*args):
	arg1, arg2 =args
	print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")
    
def print_none():
    print("I got nothing.")
    
print_two("Junhao", "Liang")
print_two_again("Junhao", "Liang")
print_one("Junhao")
print_none()
