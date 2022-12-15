if __name__ == '__main__':
    records = []
    grade = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        # lista de lista
        records.append([name, score])

        # lista com as notas
        grade.append(score)

conjunto = set(grade) # conjuntos desordenado de elementos não repetidos
grade = sorted(conjunto) # ordenando os elementos

# como tenho agora um conjunto ordenado de elementos não repetidos, o segundo elemento é de fato a segunda menor nota
secondLowestScore = grade[1]

finalName = []

for i in records:
    if secondLowestScore == i[1]:
        finalName.append(i[0]) # add nomes dos alunos com a segunda menor nota

finalName.sort() # ordenando em ordem alfabetica

for n in finalName:
    print(n)