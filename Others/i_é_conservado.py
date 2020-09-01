# i é conservado, então entra com um valor no laço e sai com o valor da mudança que ocorreu dentro do laço.

i = 0

while i < 10:
    print('i dentro do laço', i)
    i = i + 1

print('i fora do laço', i)

"""
i dentro do laço 0
i dentro do laço 1
i dentro do laço 2
i dentro do laço 3
i dentro do laço 4
i dentro do laço 5
i dentro do laço 6
i dentro do laço 7
i dentro do laço 8
i dentro do laço 9
i fora do laço 10

O valor de i é conservado após sair do laço.
"""