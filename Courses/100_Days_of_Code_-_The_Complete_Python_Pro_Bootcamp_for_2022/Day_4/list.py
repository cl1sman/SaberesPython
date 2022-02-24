# basicaly start with open square bracket, and end closed square bracket. With items separeted with comma
"""example = [item1, item2] """
# in this example, we have list data structure

# normal mode, no list
"""state1 = "primeiro_estado" """
"""state2 = "segundo_estado" """

# mode list
""" states = ["primeiro_estado", "segundo_estado"] """

# change piece(s) in list
"""states[index] = "o_que_quer_mudar" """

# .append, add item in the end of list
"""states.append("item_que_vai_ser_adicionado")"""

example_extend = ["item1", "item2"]
print(example_extend)
example_extend.extend(["item3", "item4"])
print(example_extend)

# Example
"""
    fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
    fruits[-1] = "Melons"
    fruits.append("Lemons")
    print(fruits)

    output:
    ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]
"""