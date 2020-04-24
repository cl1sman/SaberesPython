# List example
prime_numbers = [2, 3, 5, 7, 11, 13]

# Tuple example
perfect_squares = (1, 4, 9, 16, 25, 36)


# Display lengths
print('# Primes = ', len(prime_numbers))
print('# Squares = ', len(perfect_squares))
print()

# Iterate over both  sequences

for p in prime_numbers:
    print('Prime: ', p)

print()

for n in perfect_squares:
    print('Square: ', n)

print()
print('List methods')
print(dir(prime_numbers))
print(80*'_')
print()

print('Tuple methods')
print(dir(perfect_squares))
print()

# more dir()
import sys

print(dir(sys))
print(help(sys.getsizeof))

print()

list_eg = [1, 2, 3, 'a', 'b', 'c', True, 3.14159] # list ocupa mais memoria que tuple
tuple_eg = (1, 2, 3, 'a', 'b', 'c', True, 3.14159)

print('List size = ', sys.getsizeof(list_eg))
print('Tuple size = ', sys.getsizeof(tuple_eg))

"""
    Difference
    List:
        * Add data
        * Remove data
        * Change data
    Tuples:
        * Cannnot be changed
        * 'Immutable"
        * Made quickly
"""