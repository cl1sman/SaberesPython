"""
  Welcome to The Boredless Tourist, an online application giving you the power to 
  find the parts of the city that fit the pace of your life. We at The Boredless 
  Tourist run a recommendation engine using Python. We first evaluate what a person’s 
  interests are and then give them recommendations in their area to venues, restaurants,
  and historical destinations that we think they’ll be engaged by. Let’s get started!
"""
import function_

test_destination_index = function_.get_traveler_location(function_.test_traveler)
print(test_destination_index)

# print(get_destination_index('Los Angeles, USA'))
# print(get_destination_index('Paris, France'))
# print(get_destination_index('Hyderabad, India'))

# get_destination_index(traveler_destination)

function_.add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
function_.add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
function_.add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
function_.add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
function_.add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
function_.add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
function_.add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
function_.add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
function_.add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
function_.add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
function_.add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


la_arts = function_.find_attractions('Los Angeles, USA', ['art'])

print(la_arts)


smills_france = function_.get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)