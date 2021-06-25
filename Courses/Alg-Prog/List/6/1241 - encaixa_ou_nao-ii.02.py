n = int(input())

for i in range(n):
    A, B = list(map(str, input().split()))
    x = len(B) # tamanho de B
    if A[-x:] == B: # Quando quero indicar que vai até o fim, posso usar [inicio:], assim ele vai até o fim. para do inicio até, posso fazer [:fim]
        print('encaixa')
    else:
        print('nao encaixa')