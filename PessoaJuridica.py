from Pessoa import Pessoa
class PessoaJuridica(Pessoa):
    def __init__(self, nome, numero_conta, data_abertura_conta, status, data_abertura_empresa, cnpj):
        super().__init__(nome, numero_conta, data_abertura_conta, status)
        self.__dataAberturaEmpresa = data_abertura_empresa
        self.__cnpj = cnpj
    @property
    def dataAberturaEmpresa(self):
        return self.__dataAberturaEmpresa
    @dataAberturaEmpresa.setter
    def dataAberturaEmpresa(self, data_abertura_empresa):
        self.__dataAberturaEmpresa = data_abertura_empresa
    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        if len(cnpj) != 18:
            raise ValueError("O CNPJ deve conter 18 caracteres (no formato 00.000.000/0001-00).")
        self.__cnpj = cnpj
