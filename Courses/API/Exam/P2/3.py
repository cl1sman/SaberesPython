população_a, população_b, crescimento_a, crescimento_b = input().split()
população_a, população_b, crescimento_a, crescimento_b = int(população_a), int(população_b), float(crescimento_a), float(crescimento_b)



anos = 0
crescimento_a += 100
crescimento_b += 100

while pa <= pb:
    pa = int((crescimento_a / 100) * população_a)
    pb = int((crescimento_b / 100) * população_b)
    anos += 1
    
print(anos)


