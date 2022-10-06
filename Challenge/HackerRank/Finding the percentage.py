# The provided code stub will read in a dictionary containing key/value 
# pairs of name:[marks] for a list of students. Print the average of the 
# marks array for the student name provided, showing 2 places after the 
# decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        # aqui tenho um dicionario com um valor que é uma lista
    query_name = input()
    add = 0
    for valuesOfKey in student_marks[query_name]: # aqui tomo o dicionario informando a chave e tomo os valores da lista (que está dentro do dicionario)
        add += valuesOfKey
    average = add / len(student_marks[query_name])
    print(f'{average:.2f}')
