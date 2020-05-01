"""
  Welcome to The Boredless Tourist, an online application giving you the power to 
  find the parts of the city that fit the pace of your life. We at The Boredless 
  Tourist run a recommendation engine using Python. We first evaluate what a person’s 
  interests are and then give them recommendations in their area to venues, restaurants,
  and historical destinations that we think they’ll be engaged by. Let’s get started!
"""

destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wikes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

# print(get_destination_index('Los Angeles, USA'))
# print(get_destination_index('Paris, France'))
# print(get_destination_index('Hyderabad, India'))

# get_destination_index(traveler_destination)

attractions = [[], [], [], [], []]
print(attractions)

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except SyntaxError:
    return

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions('Los Angeles, USA', ['art'])

print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]

  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = 'Hi ' + traveler[0] + ", we think you'll like these places aroung " + traveler_destination + ': '
  """ If last attraction in list add a period, else add a comma plus a space"""
  for i in range(len(traveler_attractions)):
    """Extra logic check to see if attraction we are on is the last one < if it is format the interests_string differentyly"""
    if traveler_attractions[-1] == traveler_attractions[i]:
      interests_string += 'the ' + traveler_attractions[i] + '.'
    else:
      interests_string += 'the ' + traveler_attractions[i] + ', '
  return interests_string
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)