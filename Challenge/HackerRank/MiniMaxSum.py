# Given five positive integers, find the minimum and maximum
# values that can be calculated by summing exactly four of 
# the five integers. Then print the respective minimum and 
# maximum values as a single line of two space-separated long integers. 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arrSum = 0
    arrSumTotal = []
    length_arr = len(arr)
    
    for _ in range(length_arr):
        arrSum = 0
        for i in range(length_arr):
            if i != _:
                arrSum += arr[i]
            
        arrSumTotal.append(arrSum)
        
    minSum = arrSumTotal[0]
    maxSum = arrSumTotal[0]
    
    for index in arrSumTotal:
        # great or lower
        if index > maxSum:
            maxSum = index
        # I need check min either. So, if. No elif
        if index < minSum:
            minSum = index
    
    return print(f"{minSum} {maxSum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)