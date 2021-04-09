#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

code_product1, units_product1, price_product1 = input().split()
code_product1, units_product1, price_product1 = int(code_product1), int(units_product1), float(price_product1)

code_product2, units_product2, price_product2 = input().split()
code_product2, units_product2, price_product2 = int(code_product2), int(units_product2), float(price_product2)

print(f'VALOR A PAGAR: R$ {(units_product1*price_product1) + (units_product2*price_product2):.2f}')

exit(0)