# from <https://www.journaldev.com/32742/python-remove-duplicates-from-list>
"""
    We can create a list from an iterable 
    using the list comprehension. This 
    technique is the same as using the 
    temporary list and the for loop to 
    remove the duplicate elements. But, it 
    reduces the number of lines of the code.
"""
lista_inteiros = [1, 2, 3, 4, 3, 2]
temp = []
[temp.append(x) for x in lista_inteiros if x not in temp]
print(temp)