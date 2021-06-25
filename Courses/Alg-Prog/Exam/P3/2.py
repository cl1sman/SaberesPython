A = []
m = int(input())
n = int(input())
for i in range(m):
    A.append([int(j) for j in input().split()])

tamanho = len(A)

def ordenada(A):
    for i in range(m):
        for j in range(n-1):
            anterior = A[i][j]
            if anterior < A[i][j+1]:
                True
            else:
                False

ordenada(A)


                verdade = 0
                if A[i][j] < A[i][j+1]:
                    verdade = True
                else:
                    verdade = False


####################################################
def ordenada(A):
    anterior = A[0][0]
    teste = True # enquanto o teste for verdadeiro
    for i in A: # pega as lista de A
        for j in i: # pega o elemento da lista
            if j < anterior:
                teste = False
            anterior = j
    return teste

m, n = input().split()
m, n = int(m), int(n)

A = []
for i in range(m):
    A.append([int(i) for i in input().split()])

print(ordenada(A))
###############################################

###############################################
A = []
m = int(input())
n = int(input())
for i in range(m):
    A.append([int(j) for j in input().split()])

def ordenada(A):
    teste = True
    for i in range(m):
        for j in range(n-1):
            ultimo = A[i][j+1]
            
        if ultimo > A[i+1][0]:
            teste = False

ordenada(A)
##################################################