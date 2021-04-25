"""
    Observe o algoritmo abaixo, que dada uma frase determina
    quantos espaços a frase contém.

        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-
        frase = input("Informe uma frase: ")
        esp = i = 0
        while i < len(frase):
            if frase[i] == ' ':
                esp += 1
            i += 1
        print("A frase tem %d espaços" % esp)
        exit(0)

    Escreva um programa que, dada uma cadeia de caracteres, conte
    a quantidade de letras minúsculas, letras maiúsculas, dígitos,
    espaços e símbolos de pontuação que essa cadeia possui
    (considere que se um caractere não é letra, nem dígito e nem
    espaço, então é uma pontuação). Dica: digite help(str) no
    console do Python e procure funções que ajudem nesse exercício.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
frase = input("Informe uma frase: ")
esp = decimal = digito = minusculo = maiusculo = numerico = pontuacao = i = 0
while i < len(frase):
    if frase[i] == ' ':
        esp += 1
    elif frase[i].isdecimal():
        decimal += 1
    # elif frase[i].isdigit():
    #     digito += 1
    elif frase[i].islower():
        minusculo += 1
    elif frase[i].isupper():
        maiusculo += 1
    # elif frase[i].isnumeric():
    #     numerico += 1
    else:
        pontuacao += 1
    i += 1
print(f"A frase tem {esp} espaços, {minusculo} minúsculas, {maiusculo} maiúsculas, {decimal} dígitos, {pontuacao} pontuação")
exit(0)