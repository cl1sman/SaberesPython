"""
Qualquer número natural de quatro algarismos pode ser dividido em duas dezenas formadas peloes seus dois primeiros e dois últimos dígitos. Por exemplo 9712 = 97 e 12; 5134 = 51 e 34. Com base nisso, faça um algoritmo que lê 'apenas um númerro inteiro de n (de 4 algarismos) e verifica se a raiza quadrada de n é igual a soma das duas dezenas que compõem n. Informando que "Sim, raiz quadrada igual a soma das duas dezenas" ou "Não, raiz quadra não é igual a soma das duas dezenas".
Como exemplo, suponha que o valor de n lido pelo algoritmo foi 9801. As duas dezenas de n são 98 e 01, soma de dessas dezenas é igual a 99 (98 + 01), raiz quadrada de n = 99. Portanto, a raiz quadrada de 9801 é igual a soma de suas dezenas.
"""
import math

n = int(input('Informe um número com 4 algarismos: '))

A = n // 1 % 10
B = n // 10 % 10
C = n // 100 % 10
D = n // 1000 % 10

primeiro_par = str(D) + str(C)
segundo_par = str(B) + str(A)

soma = int(primeiro_par) + int(segundo_par)
raiz = math.sqrt(n)

if soma == raiz:
    print('Sim, raiz quadrada igual a soma das duas dezenas')
else:
    print('Não, raiz quadrada não é igual a soma das duas dezenas')
print(soma)
