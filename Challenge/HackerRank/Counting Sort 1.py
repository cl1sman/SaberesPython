#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    # max() for know greater number
    newArray = [0] * (max(arr) + 1) # create [0, 0, ..., 0]. +1 pra contagem incluir o 0 (de 0 a n)
    for i in range(len(newArray)):
        newArray[i] = arr.count(i) # count(i) conta quantas vezes i apareceu no array
    return
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
