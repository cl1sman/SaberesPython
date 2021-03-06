# instanciando classes

from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

# objeto 'a'
a = PessoaFisica('111.222.333-44', nome='Alfredo', idade=22)

print(a.get_CPF())
print(a.get_nome())
print(a.get_idade())

b = PessoaJuridica('64.614.527/0001-99', nome='Empresa X', idade=22)

print(b.get_CNPJ())
print(b.get_nome())
print(b.get_idade())
