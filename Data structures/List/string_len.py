# Usando o len()
def get_length_normal(word):
    number_characters = len(word)
    return number_characters

test1 = get_length_normal('carlos')
print(test1)

# Sem usar o len()
def get_length(string):
    count = 0
    for letter in string:
        count += 1
    return count

test2 = get_length('casa')
print(test2)