class Pessoa:
    def __init__(self, nome, numero_conta, data_abertura_conta, status=False):
        self.__nome = nome
        self.__numeroConta = numero_conta
        self.__dataAberturaConta = data_abertura_conta
        self.__status = status
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @property
    def numeroConta(self):
        return self.__numeroConta
    @numeroConta.setter
    def numeroConta(self, numero_conta):
        self.__numeroConta = numero_conta
    @property
    def dataAberturaConta(self):
        return self.__dataAberturaConta
    @dataAberturaConta.setter
    def dataAberturaConta(self, data_abertura_conta):
        self.__dataAberturaConta = data_abertura_conta
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status):
        self.__status = status
    def imprimir_detalhes(self):
        attrs = vars(self)
        print('Detalhes da instância da classe Pessoa:')
        print(', '.join("%s: %s" % (key[2:], value) for key, value in attrs.items()))