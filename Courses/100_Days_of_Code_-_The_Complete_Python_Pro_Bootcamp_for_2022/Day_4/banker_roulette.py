# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
print(names[random.randint(0, len(names) - 1)] + " is going to buy the meal today.")
"""
    step-by-step
    tenho uma lista, e preciso especificar o index
    
        lista[]

    este index, ou seja, este número deverá ser randomico, para que possa escolher
    de forma randomica um item da lista
    para isso:
        
        random.randint(start, end)
    
    O fim (end) será o tamanho da lista, então devo usar o len()
        
        len(names)

    Mas, como o len() retorna o total de itens que há na lista, devo subtrair 1,
    porque senão terei um erro:
         
         print(names[random.randint(0, len(names))])
    IndexError: list index out of range

    O len() retorna o total de itens da lista, a quantidade, já o index é a posição
    nesta lista, porém, o index inicia em 0. Por isso - 1

    Desta forma, o len() retorna a quantidade de itens. O index trata das posições,
    e inicia em zero. Logo, subtraio 1.
"""