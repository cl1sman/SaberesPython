principal = int(input('Enter the loan principal: '))
option_for_calc = input(r"""What do you want to calculate?
type \"m\" for number of monthly payments,
type \"p\" for the monthly payment: """)

if option_for_calc == 'm':
   payment_monthly = int(input('Enter the monthly payment: '))
   if principal % payment_monthly == 0:
      periods = principal // payment_monthly
      if periods == 1:
         print('It will take {} month to repay the loan'.format(periods))
      else:
         print('It will take {} months to repay the loan'.format(periods))
   else:
      periods = (principal // payment_monthly) + 1
      print('It will take {} months to repay the loan'.format(periods))

if option_for_calc == 'p':
   periods = int(input('Enter the number of months: '))
   payment = int(principal / periods)
   if principal % periods == 0:
      print('Your monthly payment = {}'.format(str(payment)))
   else:
      monthly_payment = principal - (periods - 1) * payment
      lastpayment = principal - (monthly_payment * (periods - 1))
      print('Your monthly payment = {} and the last payment = {}'.format(monthly_payment, lastpayment))