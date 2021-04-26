A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

pi = 3.14159

triangle = 1/2 * A * C
circle = pi * C ** 2
trapezium = ((A + B) / 2) * C
square = B * B
rectangle = A * B

print(f'TRIANGULO: {triangle:.3f}')
print(f'CIRCULO: {circle:.3f}')
print(f'TRAPEZIO: {trapezium:.3f}')
print(f'QUADRADO: {square:.3f}')
print(f'RETANGULO: {rectangle:.3f}')