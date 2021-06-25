def cria_matriz(num_linhas, num_colunas):
    ''' (int, int, valor) -> matriz (lista de listas)
    Cria e retonr uma matriz com num_linhas linhas e num_colunas
    colunas em queu cada elemento é digitado pelo usuário.
    '''
    matriz = [] # lista vazia
    for i in range(num_linhas): # esse for vai repetir num_linhas vezes. se for 10, vai repetir 10 vezes, iniciando no 0 e indo até o 9
        # cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas): # o numero de vezes que este for vai repetir é o numero de num_colunas
            valor = int(input(f'Digite o elemento [{str(i)}][{str(j)}]'))
            linha.append(valor)

        # adiciona linha à matriz
        matriz.append(linha)
    return matriz

def leMatriz():
    linhas = int(input('Digite o número de linhas da matriz: '))
    colunas = int(input('Digite o número de colunas da matriz: '))
    
    # criar uma variavel e salvar a matriz, ou return matriz
    return cria_matriz(linhas, colunas)
