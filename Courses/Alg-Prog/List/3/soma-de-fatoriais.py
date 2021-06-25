while True:
  try:  
    X, Y = input().split()
    X, Y = int(X), int(Y)
    
    def fatorial(n):
        i = 1
        nfatorial = 1

        while i <= n:
            nfatorial = nfatorial * i
            i += 1
        return nfatorial    

    def soma(x, y):
        if X != 0:
            soma1 = fatorial(x)
        else:
            soma1 = 0
        
        if Y != 0:
            soma2 = fatorial(y)
        else:
            soma2 = 0
        return soma1 + soma2

    print(soma(X, Y))

  except EOFError:
    break