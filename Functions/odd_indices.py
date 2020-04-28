"""
    Create a function named odd_indices() that has one parameter named lst.
    The function should create a new empty list and add every element from
    lst that has an odd index. The function should then return this new list.
    
    For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].
"""

#Write your function here
def odd_indices(lst):
  new_list = [] # Lista vazia
  for index in range(1, len(lst), 2):
    new_list.append(lst[index])
  return new_list

"""
    for index in range(1, len(lst), 2)

    index vai receber elemento por elemento da função range()

    a função range() vai começar em 1 porque quero os elementos impares, 
    assim, start: 1, stop: len(lst), step: 2
    start: 1, vai começar em um por ser zero um elemento par.
    stop: len(lst), len() vai contar a quantidade de elementos, no caso len() vai contar a quantidade
    de elementos da lista, a lista lst vai receber os elementos passador pela chamada da função.
    step: 2 é que vai de dois em dois, então começando em 1, vai para 3, depois 5 e etc.

"""

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))