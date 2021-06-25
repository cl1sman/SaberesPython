# sequencia, i, j = input().split()

# def conta_ocorrencias(n, d):
#     x = somai = somaj = 0

#     while x < len(sequencia):
#         for _ in sequencia:
#             if _ == i:
#                 somai += 1
#         for _ in sequencia:
#             if _ == j:
#                 somaj += 1
#         x += 1

#     if somai == somaj:
#         print('S')
#     else:
#         print('N')
# conta_ocorrencias(i, j)

#######################################################
# sequencia, i, j = input().split()
# sequencia, i, j = int(sequencia), int(i), int(j)

# def conta_ocorrencias(n, d):
#     global sequencia

#     somai = somaj = 0
#     while sequencia > 0:
#         test = sequencia % 10
#         if test == i:
#             somai += 1
#         if test == j:
#             somaj += 1

#         sequencia //=  10
#     if somai == somaj:
#         print('S')
#     else:
#         print('N')
#######################################################


sequencia, i, j = input().split()
sequencia, i, j = int(sequencia), int(i), int(j)

def conta_ocorrencias(n, d):

    soma = 0
    while n > 0:
        test = n % 10
        if test == d:
            soma += 1

        n //=  10
    return soma
if conta_ocorrencias(sequencia,i) == conta_ocorrencias(sequencia, j):
    print('S')
else:
    print('N')