A, B, C = input().split()
A, B, C = int(A), int(B), int(C)

maior = (A + B + abs(A-B)) / 2

if maior < C:
    maior = C
print(f'{int(maior)} eh o maior')