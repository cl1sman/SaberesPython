sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]] # uma lista com três listas

scoops_sold = 0
for location in sales_data: # locantion vai receber item a item, primeiro index[0] (ou primeira posição, que no caso é zero(0)), depois index[1] e assim vai até terminar. location é uma variavel temporaria usada só pra andar na lista.
  print(location)
  for element in location:
    scoops_sold += element
print(scoops_sold)

# step-by-step
"""
    sales_data é uma lista que contem três listas. Assim, temos dentro de uma lista as listas na posição 0, 1 e 2
    0 - [12, 17, 22]
    1 - [2, 10, 3]
    2 - [5, 12, 13]
    location vai receber o primeiro item de sales_data, o item na posição 0
        agora location possui a lista [12, 17, 22].
        0 - 12
        1 - 17
        2 - 22
        Neste momento, entro no segundo for. No segundo loop element vai receber o primeiro item de location
        ou seja o item na posição 0, que é o inteiro 12. Depois que chegar ao item na posição 2, saio deste loop,
        retornando para o loop anterior, agora location vai receber a segunda lista, a lista da posição 2 em sales_data
    location agora recebe o segundo item de sales_date, o item na posição 1
        agora location possui a lista [2, 10, 3]
        0 - 2
        1 - 10
        2 - 3
        os proximos passos se repetem.
"""