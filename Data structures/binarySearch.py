def bynary_search(array, target):
    min = 0
    max = n-1

    if max < min:
        return -1
    mid = array[int(max/min)]
    if mid == target:
        return mid
    if mid < target:
        min = mid + 1
    else:
        max = mid -1

bynary_search([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 41)