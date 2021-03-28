"""
Elaborar um algoritmo que, leia a idade de um nadador, classificá-lo
nas categorias:
infantil A (5 - 7 anos), 
infantil B (8 - 10 anos),
juvenil A (11 - 13 anos),
juvenil B (14 - 17 anos) e
adulto (maiores que 18 anos).
"""

nadador = int(input('Idade do nadador: '))

if nadador >= 5 and nadador <= 7:
    print('infantil A')

if nadador >= 8 and nadador <=10:
    print('infanil B')

if nadador >= 11 and nadador <=13:
    print('juvenil A')

if nadador >= 14 and nadador <=17:
    print('juvenil B')

if nadador >= 18:
    print('adulto')