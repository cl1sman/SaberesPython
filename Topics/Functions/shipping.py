def ground_shipping(weight):
  if weight <= 2:
    cost = weight*1.50 + 20.0
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight*3.00 + 20.0
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight*4.00 + 20.0
    return cost
  else:
    cost = weight*4.75 + 20.0
    return cost

premium_ground_shipping = 125.0

def drone_shipping(weight):
  if weight <= 2:
    cost = weight*4.50
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight*9.00
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight*12.0
    return cost
  else:
    cost = weight*14.25
    return cost
def cheapest(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground_shipping:
    return 'Ground shipping cost less them all: ' + str(ground_shipping(weight))
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground_shipping:
    return 'Drone shipping cost less them all: ' + str(drone_shipping(weight))
  # elif premium_ground_shipping < ground_shipping(weight) and premium_ground_shipping < drone_shipping(weight):
  else:  
    return 'Premium cost less them all: ' + str(premium_ground_shipping)

x = float(input('Enter weight: '))
print()
print('Ground shipping ' + str(ground_shipping(x)))
print('Drone shipping ' + str(drone_shipping(x)))
print('Premium shipping ' + str(premium_ground_shipping))
print(cheapest(x))
print()