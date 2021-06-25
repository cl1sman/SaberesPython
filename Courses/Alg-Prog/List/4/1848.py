"""
    while (True):
  piscada_ou_grito = input()
  grito = 0
  if piscada_ou_grito == 'caw caw':
    soma += piscada_ou_grito #soma as piscadas
    grito += 1
  
  if grito == 3: #qdo der 3 gritos, para a execução.
    break
"""

"""
--*
*--
-*-
*-*
***
---
"""

# cont = 0
# soma = []
# while cont < 3:
#     entrada = input()

#     if entrada == 'caw caw':
#         cont += 1
#     else:
#         if entrada == '--*':
#             soma.append(1)

#         elif entrada == '*--':
#             soma.append(100)
#         elif entrada == '-*-':
#             soma.append(10)
#         elif entrada == '*-*':
#             soma.append(101)
#         elif entrada == '***':
#             soma.append(111)
#         elif entrada == '---':
#             soma.append(000)


# dec = 0
# while (True):
#     piscada_ou_grito = input()
#     i = 0
#     piscada = []
    
#     for _ in piscada_ou_grito:
#         if piscada_ou_grito[i] == '-':
#             fechado = 0
#             piscada.append(fechado)
#             i += 1

#         elif piscada_ou_grito[i] == '*':
#             aberto = 1
#             piscada.append(aberto)
#             i += 1
    
#     soma_piscadas = aberto
    
#     # Transformando 'piscada' que está em binário para decimal.
#     i = 0
#     for _ in piscada:
#         dec += (int(piscada[i]) * (2 ** i))  # Bin --> Dec
#         i += 1
    
#     # Verificando se houve algum grito. 
#     grito = 0
#     if piscada_ou_grito == 'caw caw':
#         print(soma_piscadas) #Imprime a soma de todas as piscadas.
#         print(dec)
#         grito += 1

#     if grito == 3:  # qdo der 3 gritos, para a execução.
#         break
piscada = [0 , 0, 1]
dec = 1
dec += (int(piscada[0]) * (2 ** 0))
dec += (int(piscada[1]) * (2 ** 1))
dec += (int(piscada[2]) * (2 ** 2))

dec = 0
while (True):
    piscada_ou_grito = input()
    i = 0
    piscada = []
    
    for _ in piscada_ou_grito:
        if piscada_ou_grito[i] == '-':
            fechado = 0
            piscada.append(fechado)
            i += 1

        elif piscada_ou_grito[i] == '*':
            aberto = 1
            piscada.append(aberto)
            i += 1
    
    soma_piscadas = aberto
    
    # Transformando 'piscada' que está em binário para decimal.
    i = 0
    for _ in piscada:
        dec += int(str(piscada[i]))  # Bin --> Dec
        i += 1
    
    # Verificando se houve algum grito. 
    grito = 0
    if piscada_ou_grito == 'caw caw':
        print(soma_piscadas) #Imprime a soma de todas as piscadas.
        print(dec)
        grito += 1

    if grito == 3:  # qdo der 3 gritos, para a execução.
        break