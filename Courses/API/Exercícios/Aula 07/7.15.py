"""
    Dado um número inteiro positivo n, verificar se este número
    contém dois dígitos consecutivos iguais.
        Exemplo:
        Se n = 23667, então n contém dois dígitos consecutivos iguais
        (66).
"""

"""
como analiso os digitos de um número?
resto, e divisão

como separar? 2834
é mais facil pegando da direita
 2834 // 10
-2830    283

"""

n = 23667

while n > 0:
    ultimo = n % 10
    n = n // 10
    penultimo = n % 10

    if ultimo == penultimo:
        print(f'contém dois dígitos consecutivos iguais: {penultimo, ultimo}')
    if penultimo > 0:
        n = n // 10

print(ultimo, penultimo, n)