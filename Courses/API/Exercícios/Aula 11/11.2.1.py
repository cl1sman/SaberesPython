def remrep(lista):
    for i in lista:
        if lista.count(i) > 1:
            lista.remove(i)
    return lista

A = [int(v) for v in input().split()]
print(remrep(A))