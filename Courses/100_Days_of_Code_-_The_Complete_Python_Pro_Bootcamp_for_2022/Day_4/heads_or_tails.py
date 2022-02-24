"""
    Using Random Module

    randint, random numbers for int
    .randint(star, end), include end

    Heads if the number 'randonmize' is 1, or Tails if 0
"""

import random

if random.randint(0, 1) == 1:
    print("Heads")
else:
    print("Tails")