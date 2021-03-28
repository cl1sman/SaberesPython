tempo = int(input())

7400 -> 2 horas = 7200
# fazer essa divisão, e vai pegando o que sobra
horas = int(tempo / 3600) # jogue fora a parte fracionaria
horas = tempo // 3600 # pega o inteiro
resto = tempo % 3600 # resto da divisão
# ao invés de usar uma outra variavel, posso usar a mesma variavel
tempo = tempo % 3600
tempo - horas * 3600 # não usamos muito, usamos mais o resto

7400 / 3600
O resto da divisão, pode ser usado
(3600 é uma hora)