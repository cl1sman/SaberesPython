"""
    Create a function named double_index that has two parameters: a list named lst and a single number named index.
    The function should return a new list where all elements are the same as in lst except for the element at index. The element at index should be double the value of the element at index of the original lst.
    If index is not a valid index, the function should return the original list.
    For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

    double_index([1, 2, 3, 4], 2)
"""

def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        new_lst = lst[:index] # a lista até o index [0, 1 como o proximo item é o index 2, eu tomo a lista até aqui. Os item da nova lista são: [3, 8]
        new_lst.append(lst[index]*2) # esta sendo adcionado o item do index escolhido que foi dobrado. Ou seja, o index*2 é adicionado ao fim da lista anterior [2, 8, -20]
        new_lst = new_lst + lst[index+1:] # aqui eu pego a lista anterior, somo os itens após o index da lista original. [2, 8, -20] + [12] = [2, 8, -20, 12]
        return new_lst

print(double_index([3, 8, -10, 12], 2))