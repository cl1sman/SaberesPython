"para que eu possa usar o resultado"

def velocidade(espaco, tempo):
    v = espaco/tempo
    return v


"mais de um comando return"
def dados(nome, idade=None):
    if(idade is not None):
        return('nome: {} \nidade: {}'.format(nome, idade))
    
    else:
        return('nome: {} \nidade: não informada'.format(nome))

"apesar de conter dois return's, ela vai apenas um"