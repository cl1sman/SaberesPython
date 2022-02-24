"""
    Basicamente o split vai dividir onde você especificar.
    E vai fazer dos "pedaços" uma lista.

    Split -> divide string (não sei se é só string)
    
    .split(","), onde tiver uma virgula "split" isso, e
    coloque em uma lista

    O que esta dentro do parenteses me dira onde haverá
    esta divisão. Se não colocar nada, será dividido
    onde tiver espaços
"""

x = "Quer comer goiaba"
print(x.split())
# output:
#   ['Quero', 'comer', 'goiaba']
print(x.split("e"))
# exatamente ond tem um "e", será feito o corte, assim, o "e" não aparece
#output:
#   ['Qu', 'ro com', 'r goiaba']