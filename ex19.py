def cheese_and_crackers(cheese_count, boxes_of_cracker):
    print(f"""
    You have {cheese_count} cheeses!
    You have {boxes_of_cracker} boxes of cracker!
    Man thas's enough for a party!
    Get a blanket.\n
    """)
print("We can just give the function numbers directly!")
cheese_and_crackers(20, 30)

print("OR, we can user variables from our script:")
amount_of_cheese = 10#global varivale1
amount_of_cracker = 50

cheese_and_crackers(amount_of_cheese, amount_of_cracker)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_cracker +1000)
