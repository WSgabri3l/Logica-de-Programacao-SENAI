# Resolver a questão do número no final.

from conta import Conta

nome = Conta(nome = 'jeremias')

nome.criarConta()

nome.deposito(valor_deposito = 100)
nome.saque(valor_saque = 170)
nome.mudarStatus()
nome.dadosConta()

nome.mostrarDict()