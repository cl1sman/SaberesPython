def mdc(a,b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

n = int(input()) - 1
MDC = int(input())
while n > 0:
    valor = int(input())
    MDC = mdc(MDC, valor)
    print(MDC)
    n -= 1