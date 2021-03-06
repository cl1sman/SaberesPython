"""
    
    Create a function named max_num() that takes a list of numbers named nums as a parameter.

    The function should return the largest number in nums

    Create a variable called maximum to track the max number, and have it start as the first 
    element in the list. Loop through all of the numbers in the list, and if a number is ever 
    greater than the current max number, the max number should be re-set to that number.
"""


#Write your function here
def max_num(nums):
  maximum = nums[0] # to track the max number
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))