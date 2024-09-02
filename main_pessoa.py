from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica
Pessoa = Pessoa("João", "12345-6", "2023-01-01", False)
Pessoa.imprimir_detalhes()
PessoaFisica = PessoaFisica("Maria", "67890-1", "2022-02-02", True, "1990-12-31", "111.222.333-44", "987654321")
PessoaFisica.imprimir_detalhes()
PessoaJuridica = PessoaJuridica("Empresa Y", "54321-9", "2021-03-03", True, "2005-06-15", "12.345.678/0001-90")
PessoaJuridica.imprimir_detalhes()

Pessoa.nome = "Carlos"
Pessoa.numero_conta = "54321-0"
Pessoa.data_abertura_conta = "2024-01-01"
Pessoa.status = True


PessoaFisica.nome = "Ana"
PessoaFisica.numero_conta = "98765-4"
PessoaFisica.data_abertura_conta = "2023-05-05"
PessoaFisica.status = False
PessoaFisica.dataNascimento = "1985-07-20"
PessoaFisica.cpf = "222.333.444-55"
PessoaFisica.rg = "123456789"

PessoaJuridica.nome = "Empresa Z"
PessoaJuridica.numero_conta = "11223-4"
PessoaJuridica.data_abertura_conta = "2022-08-08"
PessoaJuridica.status = False
PessoaJuridica.dataAberturaEmpresa = "2012-02-15"
try:
    PessoaJuridica.cnpj = "12.345.678/0001-0"
except ValueError as e:
    print(f"Erro ao atribuir CNPJ: {e}")

PessoaJuridica.cnpj = "23.456.789/0001-01"
print("\nValores modificados:")
Pessoa.imprimir_detalhes()
PessoaFisica.imprimir_detalhes()
PessoaJuridica.imprimir_detalhes()
