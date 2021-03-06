first_name = 'Matheus'
last_name = 'Silva'

def passwd_generator(first, last):
  _last_three_letter_firstName = len(first)
  _last_three_letter_lastName = len(last)

  temp_passwd = first[_last_three_letter_firstName-3:] + last[_last_three_letter_lastName-3:]
  """
    number = '12345'
    var_temp = number[1:3] # vai começar em 1 e parar na posição 3

    no caso de first[_last_three_letter_firstName-3:], seria como se temp_passwd = first[7-3:] + last[5-3:],
    a _last_three_letter_firstName recebe um valor, este valor será subtraido de -3. -3 porque quero as ultimas
    3 letras, então neste caso seria o mesmo que [7-3:]
  """

  return temp_passwd

_test_passwd = passwd_generator(first_name, last_name)
print(_test_passwd)