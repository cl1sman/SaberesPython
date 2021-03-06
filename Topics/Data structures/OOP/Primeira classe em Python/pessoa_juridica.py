from pessoa import Pessoa


class PessoaJuridica(Pessoa):
    def __init__(self, CNPJ, nome, idade):
        super().__init__(nome, idade)
        self.CNPJ = CNPJ

    def set_CNPJ(self, CNPJ):
        self.CNPJ = CNPJ

    def get_CNPJ(self):
        return self.CNPJ
