#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
(Extensão do exercício 15) Faça um programa que pergunta
quanto você ganha por hora e o número de horas trabalhadas no
mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o imposto de renda,
8% para o INSS e 5% para o sindicato. Seu programa deve
mostrar para o usuário as seguintes informações:
    * Salário bruto;
    * Quanto pagou ao INSS;
    * Quando pagou ao sindicato;
    * Salário líquido.
"""

# exercicio 15
ganho_por_hora = float(input('Valor da hora R$: '))
número_de_horas_trabalhadas_mês = float(input('Número de horas trabalhadas por mês: '))

print(f'Salario total: R${ganho_por_hora * número_de_horas_trabalhadas_mês:.2f}')

salario_bruto = ganho_por_hora * número_de_horas_trabalhadas_mês

quanto_pagou_IR = salario_bruto * 0.11
quanto_pagou_INSS = salario_bruto * 0.08
quanto_pagou_SINDICATO = salario_bruto * 0.05

salario_liquido = salario_bruto - quanto_pagou_IR -quanto_pagou_INSS - quanto_pagou_SINDICATO

print(f'Salário bruto: R${salario_bruto:.2f}')
print(f'Quanto foi pago ao INSS: R${quanto_pagou_INSS:.2f}')
print(f'Quanto foi pago ao Sindicato: R${quanto_pagou_SINDICATO:.2f}')
print(f'Salário líquido: R${salario_liquido:.2f}')

exit(0)