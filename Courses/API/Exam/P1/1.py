"""
que serão respondidas com "Sim" ou "Não

Já sabemos que o programa só será executado quando o computador não estiver ligando, então seu programa deve iniciar na primeira pergunta: "Está na tomada?".
"""

quest1 = input('Está na tomada?\n')
if quest1 == 'Não':
  print('Ligue na tomada\n')
if quest1 == 'Sim':
  quest2 = input('O monitor está ligando?\n')
  if quest2 == 'Não':
    print('Arrume o monitor\n')
  else:
    print('Arrume o computador\n')