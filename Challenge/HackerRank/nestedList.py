"""
    Given the names and grades for each student in a class of students, 
    store them in a nested list and print the name(s) of any student(s) 
    having the second lowest grade.
"""

if __name__ == '__main__':
    records = []
    grade = []
    for _ in range(int(input())): # N
        name = input()
        score = float(input())
        records.append([name, score]) # uma lista com listas records = [[name, score], [name, score], ...]
        grade.append(score) # para o calculo da 2 nota mais baixa

# para a 2nd mais baixa, crio um conjunto ordenado
grade = sorted(set(grade)) # como é um conjunto, não tem nada repetido

secondLowestScore = grade[1] # grade[0] é a menor

resultName = []

for i in records:
    if secondLowestScore == i[1]: # procurando pela nota
        resultName.append(i[0]) # aqui estou acrescentando o nome

resultName.sort()

for n in resultName:
    print(n)

# menor de todos
# menor = min([records[i][1] for i in range(len(records))]) gostei disso, mas nem sei como usar