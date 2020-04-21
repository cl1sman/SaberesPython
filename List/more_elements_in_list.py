"""
    Write a function named larger_list that has two parameters named lst1 and lst2.

    The function should return the last element of the list that contains more elements.
    If both lists are the same size, then return the last element of lst1.
"""
def larger_list(lst1, lst2):
    if len(lst1) > len(lst2):   # se a lista 1 tiver mais elementos que a lista dois, retornar o ultimo elemento da lista 1
        return lst1[-1]
    elif len(lst1) < len(lst2): # se a lista 2 tiver mais eleemntos que a lista um, retornar o ultimo elemento da lista 2
        return lst2[-1]
    else:                       # se as listas tiverem o mesmo tamanho, retornar o ultimo elemento da lista 1
        return lst1[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10, 120]))