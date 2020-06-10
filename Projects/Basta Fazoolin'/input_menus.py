from class_menus import Business, Franchise, Menu # Poderia ter usado * para dizer que era pra importar todos
# Brunch Menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
# print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))

# Early Bird Menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)
# print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

# Kids Menu
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('Kids', kids_items, 1100, 2100)

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise('1232 West End Road', menus)

new_installment = Franchise('12 East Mulberry Street', menus)

basta = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

# Arepa

arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu('Take a\' Arepa', arepas_items, 1000, 2000)

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

arepa = Business('Take a\' Arepa', [arepas_place])