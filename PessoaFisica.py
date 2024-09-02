from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, numero_conta, data_abertura_conta, status, data_nascimento, cpf, rg):
        super().__init__(nome, numero_conta, data_abertura_conta, status)
        self.__dataNascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg
    @property
    def dataNascimento(self):
        return self.__dataNascimento
    @dataNascimento.setter
    def dataNascimento(self, data_nascimento):
        self.__dataNascimento = data_nascimento
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) != 14:
            raise ValueError("O CPF deve conter 14 caracteres (no formato 000.000.000-00).")
        self.__cpf = cpf
    @property
    def rg(self):
        return self.__rg
    @rg.setter
    def rg(self, rg):
        self.__rg = rg