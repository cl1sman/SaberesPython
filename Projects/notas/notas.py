# Calculo de notas
# * entrar com quantidades de provas, trabalhos e afins. Informar os pesos.
# * salvar em arquivo. Quando abrir, exibir informações que já estão no arquivo.

# quantidade de provas em vetor?

while True:
    try:
        qtd_provas = int(input('Quantas provas? '))
        break
    except ValueError:
        print('Digite um número inteiro')
provas = []
for i in range(qtd_provas):
    provas.append(float(input('Nota da prova {}: '.format(i+1))))

pesos = list(map(float, input('Pesos das provas: ').split()))
media = sum([provas[i]*pesos[i] for i in range(qtd_provas)])/sum(pesos)
