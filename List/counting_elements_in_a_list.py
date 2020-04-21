letters = ['m', 'a', 't', 't', 'h', 'e', 't', 'r']
num_t = letters.count('t')
print(num_t)

# exemplo
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
print(jake_votes)

'''
    Caso não necessite armazenar os elementos, pode apenas printar:
    print(votes.count('Jake'))
'''