the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3,'qiarters']

for number in the_count:
    print(f"This is count {number}")#start with one
    
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
    
for i in change:
    print(f"I got {i}")

elements = []

for i in range(0,6):
    print(f"Adding {i} to the list")
    elements.append(i)#add data to the last of the list

for i in elements:
    print(f"Element was {i}")