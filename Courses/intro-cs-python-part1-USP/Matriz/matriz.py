def cria_matriz(num_linhas, num_colunas, valor):
    ''' (int, int, valor) -> matriz (lista de listas)
    Cria e retonr uma matriz com num_linhas linhas e num_colunas
    colunas em queu cada elemento é igual ao valor dado.
    '''
    matriz = [] # lista vazia
    for i in range(num_linhas): # esse for vai repetir num_linhas vezes. se for 10, vai repetir 10 vezes, iniciando no 0 e indo até o 9
        # cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas): # o numero de vezes que este for vai repetir é o numero de num_colunas
            linha.append(valor)

        # adiciona linha à matriz
        matriz.append(linha)
    return matriz
