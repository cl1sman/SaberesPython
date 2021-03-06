"Exercicio do HackerRank"

"""
    if __name__ == '__main__':
        a = int(input())
        b = int(input())
"""

"Parece ser um variavel especial 'special variables'"

import math

def functionA():
    print('Function A')

def functionB():
    print('Function B {}'.format(math.sqrt(100)))

print('before __name__ guard')
if __name__ == '__main__':
    functionA()
    functionB()
print('after __name__ guard')