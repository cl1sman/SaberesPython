def minion_game(string):
    # your code goes here
    consonants = 0  # Stuart has to make words starting with consonants.
    vowels = 0  # Kevin has to make words starting with vowels.

    for i in range(len(string)):
        if string[i] in 'AEIOU':
            vowels += len(string) - i
        else:
            consonants += len(string) - i
    """
        O problema é facil de resolver, preciso apenas trabalhar com as possibilidades que formam a partir de cada letra
        junto ao restante da palavra.
        BANANA = 6 possibilidades
        B BA BAN BANA BANAN BANANA
        ANANA = 5 possibilidades
        A AN ANA ANAN ANANA
        ...

        Desta forma, pasta um for para percorrer a string. Com o indice, sei onde começa a substring, bastando calcular
        as possibilidades: tamanho da string - a posição atual
    """
    if vowels > consonants:
        print(f'Kevin {vowels}')
    elif vowels < consonants:
        print(f'Stuart {consonants}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
