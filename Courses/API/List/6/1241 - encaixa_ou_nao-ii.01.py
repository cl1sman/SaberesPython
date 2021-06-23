n = int(input())

for i in range(n):
    A, B = list(map(str, input().split()))
    if A[-len(B):] == B:
        print('encaixa')
    else:
        print('nao encaixa')