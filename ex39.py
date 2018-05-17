states = {
    'Oregon':'OR',
    'Florida':'FL',
    'Califoria':'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
print(states['Oregon'])

cities = {
    'CA':'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

print(cities[states['Califoria']])

cities['NY']= "New York"
cities['OR']= 'Portland'

print('-'*20)
print("NY State has:",cities['NY'])
print("NY State has:",cities['OR'])

print('-'*20)
print("Michigan has:",cities[states['Michigan']])
print("Florida has :",cities[states['Florida']])

print('-'*20)
print(states.items())
print(list(states.items()))
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-'*20)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}" )
    print(f"and has city {cities[abbrev]}" )
    
print('-'*20)

state = states.get('Texas')

if not state:
    print("sorry, no Texas")

##cities['TX']= "12"
city = cities.get('TX', "Does Not Eixst")#return second value if the first
#parament does not exist
print(f"The city for the state 'Tx' is: {city}")
