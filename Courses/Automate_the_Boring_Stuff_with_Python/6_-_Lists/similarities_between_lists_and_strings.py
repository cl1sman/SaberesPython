# Variables
spam = 42
cheese = spam
spam = 100 # change spam, but cheese is not changed
print(spam) # output: 100
print(cheese) # 42. The data is not changed

"""
    But, When you assign a list to a variable you're actually
    assigning a list reference to the variable and references a
    value that points to some bbit of data like a list.
"""

# List
spam_2 = [0, 1, 2, 3, 4, 5]
cheese_2 = spam # assing to reference. if modify, I modify the spam_2. Não é uma copía, mas um referencia
cheese_2[1] = "Hello!" # quando eu "modifico aqui", estou modificando a partir de uma referencia onde a lista de fato está
print(cheese_2) # output: [0, "Hello!", 2, 3,  4, 5]
print(spam_2) # output: [0, "Hello!", 2, 3,  4, 5]