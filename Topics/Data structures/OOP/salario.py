class Funcionario:
  def __init__(self, nome, salario_base, horas_extras, valor_da_hora):
    self.nome = nome
    self.salario_base = salario_base
    self.horas_extras = horas_extras
    self.valor_da_hora = valor_da_hora

  def salario(self):
    return """
    Nome: {nome}
    Salario: {salario}
    Horas Extras: {horas}
    Valor das horas extras: {v_horas}
    Salario com extras: {salario_extra}
    """.format(nome=self.nome, salario=self.salario_base, horas=self.horas_extras, v_horas=self.valor_da_hora, salario_extra=(self.salario_base + (self.horas_extras * self.valor_da_hora)))

funcionario1 = Funcionario('Clisman', 1000, 10, 20)
print(funcionario1.salario())