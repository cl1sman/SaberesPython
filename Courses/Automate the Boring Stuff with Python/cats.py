"""
print('How many cats do you have?')
numCats = input()
if int(numCats) >= 4:
    print('Trat is a lot of cats.')
else:
    print('That is not tha many cats.')
"""

# other made for this

print('How many cats do you have?')
numCats = input()

try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')
