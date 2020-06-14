"""
    IMC - Índice de Massa Corpórea, parâmetro adotado pela Organização
    Mundial de Saúde para calcular o peso ideal de cada pessoa.

    IMC                     Classificação           Obesidade (grau)
    Menor que 18.5          Magreza                 0
    Entre 18.5 e 24.9       Normal                  0
    Entre 25.0 e 29.9       Sobrepeso               I
    Entre 30.0 e 39.9       Obesidade               II
    Maior que 40.0          Obesidade grave         III
"""

def IMC(peso, altura):
    IMC = peso / (altura ** 2)
    return IMC