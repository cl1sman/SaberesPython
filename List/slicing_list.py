suitcase = ['shirt', 'calça', 'books']
beginning = suitcase[0:2]
print(beginning)
middle = suitcase[1:2]
print(middle)

# posso omitir onde inicia, caso inicie a lista desde o começo, ou o fim, caso vá até o fim
itens = ['abobora', 'noiva', 'trapo', 'caixa', 'operador de celular']
inicio = itens[:3] # como a lista vai iniciar do incio, não preciso informar, pois entende-se que vai começar do index 0
fim = itens[-2:] # como quero a lista até o ultimo elemento, não necessito informar o ultimo item
"""
    Usando negativo, é como se a contagem fosse do fim para o começo. Então se quiser os três ultimos itens
    basta informar -3. -1 é o ultimo, -2 o penultimo e -3 o antepenultimo.
"""