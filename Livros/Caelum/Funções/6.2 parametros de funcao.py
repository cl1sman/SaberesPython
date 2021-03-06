"Para um parâmetro ser opcional, o mesmo é atribuído a um valor padrão(default) - o mais comum é utilizar None"
"O atributo nome é obrigatorio"
def dados(nome, idade=None):
    print('nome: {}'.format(nome))
    
    if(idade is not None):
        print('idade: {}'.format(idade))
    else:
        print('idade: não informada')