def somapar(x):
    i = 0
    somapar = 0

    while i < 5:

        if x % 2 == 0:
            somapar += x
            i += 1
        x = x + 1
    return somapar

x = int(input())
while x != 0:
    print(somapar(x))
    x = int(input())