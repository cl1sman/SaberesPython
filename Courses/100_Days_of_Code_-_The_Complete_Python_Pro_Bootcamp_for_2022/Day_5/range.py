## Definition and Usage

"""
Definição e uso:

    A função range() retorna uma sequencia de numeros, começando por zero (por padrão), e
    acrescendo 1 (por padrão), e parando antes do número especifico (assim, o parametro de 
    parada não é incluido)

Sintaxe:

    range(start, stop, step)

Parameter Values

    start: Optional. An integer number specifying at which position to start. Default is 0
    stop: Required. An integer number specifying at which position to stop (not included).
    step: Optional. An integer number specifying the incrementation. Default is 1

Good source: https://www.w3schools.com/python/ref_func_range.asp
"""

# 100 + 99 + 98 + ... 4 + 3 + 2 + 1
sum_ = 0
for number in range(101):
    sum_ += number
print(sum_)