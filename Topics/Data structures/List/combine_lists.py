"""
    Write a function named combine_sort that has two parameters named lst1 and lst2.
    The function should combine these two lists into one new list and sort the result. Return the new sorted list.
"""

def combine_sort(lst1, lst2):
    combine_lists = lst1 + lst2
    combine_lists = sorted(combine_lists) # why using sorted()? .sort() do not return anything. sort() does not return anything. Só vai ordenar, e não poderá usar os valores, com sorted() sim.
    return combine_lists

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))