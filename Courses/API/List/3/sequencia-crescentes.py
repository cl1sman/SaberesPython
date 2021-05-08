# parar quando for zero
X = int(input())


stop = False
while stop == False:
    i = 1

    while i == 1:
        print(f'{i}', end='')
        i += 1

        while i <= X:
            while i == 1:
                print(f'{i}', end='')
                i += 1
            print(f' {i}', end='')
            i += 1
        X = int(input('\n'))
        if X == 0:
            stop = True


    # X = int(input('\n'))
    # if X == 0:
    #     stop = True
exit(0)