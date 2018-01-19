# _*_ coding: UTF-8 _*_

# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# states['Texas'] = 'TX'

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
# cities['TX'] = 'Xian'

# print some cities
print ('_'*10)
print ('NY State has: ', cities['NY'])
print ('OR State has: ', cities['OR'])

# print some states
print ('_'*10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print ('_'*10)
print ('Michigan has: ', cities[states['Michigan']])
print ('Florida has: ', cities[states['Florida']])

# print every city in state
print ('_'*10)
for state,abbrev in states.items():
    print ('%s state is abbreviated %s and has city %s' %(
        state,abbrev,cities[abbrev]))

print ('_'*10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print ('Soory, no Texas.')

# get a city with a default value
city = cities.get('TX','Does not Exist')
print ('The city for the state \'TX\' is: %s'  % city)
