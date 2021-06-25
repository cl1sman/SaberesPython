# a) uma função que receba uma lista e remova elementos repeditos.
def remrep(lista):
    final_list = []
    for i in lista:
        if i not in final_list: # se não estiver na nova lista, eu adiciono
            final_list.append(i)
    return final_list

A = [int(v) for v in input().split()]
print(remrep(A))