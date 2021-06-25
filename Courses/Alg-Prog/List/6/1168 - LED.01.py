n = int(input())

for i in range(n):
    led = 0
    x = input()

    for j in x:
        if j == '0':
            led += 6
        if j == '1':
            led += 2
        if j == '2':
            led += 5
        if j == '3':
            led += 5
        if j == '4':
            led += 4
        if j == '5':
            led += 5
        if j == '6':
            led += 6
        if j == '7':
            led += 3
        if j == '8':
            led += 7
        if j == '9':
            led += 6
    print(f'{led} leds')