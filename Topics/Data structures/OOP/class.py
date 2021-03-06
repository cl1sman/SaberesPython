class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last) #antes: .format(emp_1.first, ...), para ficar mais generico, e ser reutilizavel, usa self
    
emp_1 = Employee('Matheus', 'Clisman', 50000) # passo os argumento. e faço deste um objeto
emp_2 = Employee('Test', 'User', 9000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

# run in background
print(emp_1.fullname()) # não necessita de argumento
print(Employee.fullname(emp_1)) # precisa de argumento