items_on_sale = ['blue_shirt', 'striped_socks', 'knit_dress', 'red_headband', 'dinosaur_onesie']

print('Checking the sale list!')
for item in items_on_sale:
    print(item)
    if item == 'knit_dress':
        break                   # se não tivesse o break, o programa continuaria, então se houvesse 100000 itens depois, o loop continuaria
    print('End of serach!')