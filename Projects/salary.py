employee_numer = int(input('employee\'s number: '))
worked_hours_number_month = float(input('worked hours: '))
received_per_hour = float(input('Received per hour: '))

print(f'NUMBER = {employee_numer}')
print(f'SALARY = U$ {worked_hours_number_month * received_per_hour:.2f}')