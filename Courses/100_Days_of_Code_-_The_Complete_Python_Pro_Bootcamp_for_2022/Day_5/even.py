# Sum even: 1 to 100
# Two ways

# 1 - using module
sum_even1 = 0

for _ in range(1, 101):
    if _ % 2 == 0:
        sum_even1 += _

print(sum_even1)

# 2 - using "step size" 2 in range

sum_even2 = 0

for _ in range(2, 101, 2):
    sum_even2 += _

print(sum_even2)