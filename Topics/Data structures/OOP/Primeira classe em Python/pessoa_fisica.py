from pessoa import Pessoa


class PessoaFisica(Pessoa):
    """
        Dentro do contrutor, precisamos passar quais atributos, a classe
        pessoa fisica precisa possuir, para que consiga herdar da classe pessoa
    """
    def __init__(self, CPF, nome, idade):
        super().__init__(nome, idade)
        self.CPF = CPF
    
    def set_CPF(self, CPF):
        self.CPF = CPF
    
    def get_CPF(self):
        return self.CPF
