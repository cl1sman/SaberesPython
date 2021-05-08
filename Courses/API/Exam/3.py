a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

if a == b == c:
    print('Equilátero')
elif a == b or a == c or b == c:
    print('Isósceles')
elif a != b != c:
    print('Escaleno')