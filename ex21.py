def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
def multiply(a, b):
    print(f"MULTIPLE {a} * {b}")
    return a * b
def devide(a, b):
    print(f"DEVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")
age = add(30,5)
height = subtract(78, 4)
weight = multiply (90, 2)
iq = devide(100, 2)

print(f"Age: {age}, height: {height}, weight: {weight}, iq: {iq}")

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight,devide(iq, 2))))

print(f"That become:", what, "Can you do it by hand?")
