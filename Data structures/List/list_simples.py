# Lista
lista = ['Jorge', 51, 'Carlos', 62]

# Lista de listas
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]
ages = [['Aaron', 15], ['Dhruti', 16]]

# exemplos
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = []
age.append(42)
print(age)

all_ages = [32, 41, 29] + age
print(all_ages)

name_and_age = zip(first_names, all_ages)
print(name_and_age)
print(list(name_and_age))

ids = range(4)
print(ids)