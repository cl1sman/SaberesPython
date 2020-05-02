# Lists
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']
test_traveler = ['Erin Wikes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[], [], [], [], []]

# Functions
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except SyntaxError:
    return

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