names = ['Carlos', 'John']
print(names)
ages = [21, 34]
print(ages)

names_and_ages = zip(names, ages)
print(names_and_ages)

list_names_add_ages = list(names_and_ages)
print(list_names_add_ages)
print(list_names_add_ages[0])

"""
    names e ages serão unidos. como a primeira lista é names, na posição zero terei
    o primeiro nome, após a virgula a idade. Logo, 'Carlos', 21. Porque ambos item 
    estão na posição zero. 'Carlos' e 21 estarão na primeira posição depois que u-
    nir as listas usando zip.
"""