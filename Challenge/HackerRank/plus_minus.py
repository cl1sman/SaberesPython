# Given an array of integers, calculate the ratios of its elements that are positive, 
# negative, and zero. Print the decimal value of each fraction on a new line with 
# places after the decimal.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    total = len(arr)
    # Test positve, negative and zeros values
    # Tomar cuidado com divisao por zero
    positive = 0
    negative = 0
    zero = 0
    for _ in arr:
        if _ > 0:
            positive += 1
        elif _ < 0:
            negative += 1
        else:
            zero += 1
    
    # print proportions values
    print(positive / total)
    print(negative / total)
    print(zero / total)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)