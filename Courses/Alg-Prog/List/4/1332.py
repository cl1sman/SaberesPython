# n_palavras = int(input())

# one = 'one'
# two = 'two'
# three = 'three'
# word = input()

# i = 0
# cont = 0
# while i < 3:
#     if one[i] == word[i]:
#         pass
#     else:
#         cont += 1
#     i += 1

# print(cont)

quantas_vezes = int(input())

while quantas_vezes > 0:
    texto = input()
   
    if(len(texto)>3):
        print(3)
    else:
        soma = 0
        if (texto[0:1]=='o'):
            soma += 1
        if (texto[1:2]=='n'):
            soma += 1
        if (texto[2:3]=='e'):
            soma += 1
       
        if(soma>=2):
            print(1)
        else:
            print(2)
    quantas_vezes -= 1