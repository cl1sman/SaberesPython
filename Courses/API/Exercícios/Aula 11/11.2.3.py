def remrep(lista):
    i = 0
    while i < len(lista):
        if lista.count(lista[i]) > 1:
            lista.remove(lista[i])
        else:
            i += 1 # acrescentar o i, apenas se eu não remover
