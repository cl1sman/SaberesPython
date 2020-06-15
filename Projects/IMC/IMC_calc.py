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
    indice_massa_comporea = float(IMC)
    
    if indice_massa_comporea < 18.5:
        print("""\nIMC                     Classificação           Obesidade (grau)
                 Menor que 18.5          Magreza                 0""")
    elif indice_massa_comporea >= 18.5 and IMC <= 24.9:
        print("""\nIMC                     Classificação           Obesidade (grau)
Entre 18.5 e 24.9       Normal                  0\n""")
    elif indice_massa_comporea >= 25.0 and IMC <= 29.9:
        print("""\nIMC                     Classificação           Obesidade (grau)
Entre 25.0 e 29.9       Sobrepeso               I\n""")
    elif indice_massa_comporea >= 30.0 and IMC <= 39.9:
        print("""\nIMC                     Classificação           Obesidade (grau)
Entre 30.0 e 39.9       Obesidade               II\n""")
    elif indice_massa_comporea > 40.0:
        print("""\nIMC                     Classificação           Obesidade (grau)
Maior que 40.0          Obesidade grave         III\n""")

    return "Seu IMC: {:.2f}".format(indice_massa_comporea)