#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagonal_principal = 0
    diagonal_segundaria = 0
    for i in range(len(arr)):
        diagonal_principal += arr[i][i]
        diagonal_segundaria += arr[i][len(arr)-1-i]
    return abs(diagonal_principal - diagonal_segundaria) # len(arr) - 1 - i. O -1 é porque o indece começa em 0. O -i é para fazer o segundo index andar para trás.


# fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

# fptr.write(str(result) + '\n')

# fptr.close()
