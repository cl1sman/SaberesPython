# make manualy
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)

#   Or, using function range()
"""
    The function range() takes a single input, and generates numbers starting at 0
    and ending at the number before the input. So, if we want the numbers from 0
    through 10, we use ranges(11) because 11 is 1 greater than 10
"""

# Using range() function to make list
"""
    arguments:
    range(start, stop, step)
"""
my_range = range(11) # Just like with zip, the range function returns an object that we can convert into a list
print(my_range)
print(list(my_range)) # range retorna um object, então preciso converter para uma list

# Posso passar mais de um argumento

my_new_list = range(2, 9) # start 2 and ending at 8 (just before 9)
print(list(my_new_list)) # range() retorna um object. converto para list()