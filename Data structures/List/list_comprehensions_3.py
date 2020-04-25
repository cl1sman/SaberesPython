# Um exemplo mais elaborado
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

new_prices = [price - 5 for price in prices]

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)

# Reescrevendo
cortes_abaixo_de_30 = []
for i in range(len(new_prices)):
  if new_prices[i] < 30:
    cortes_abaixo_de_30.append(hairstyles[i])
print('Corte abaixo de 30 usando loop: ', cortes_abaixo_de_30)