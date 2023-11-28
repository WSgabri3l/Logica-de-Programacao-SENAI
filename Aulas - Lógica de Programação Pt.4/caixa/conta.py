class Conta:

    def __init__(self, nome):

        self.nome = nome
        self.lista_de_usuário = []

    def criarConta(self):

        # Cria uma cópia do nome inserido.

        self.nome_copia = self.nome
        self.lista_de_usuário.append(self.nome)

        # Cria dicionário com as informações do indivíduo.

        self.nome = {'nome' : self.nome_copia, 
                    'status' : 'ativado', 
                    'numero': None, 
                    'saldo' : 0}
        

    def exibirSaldo(self):

        print(f"\nSaldo da Conta: {self.nome['saldo']}")

    def dadosConta(self):

        print(f"\nNome: {self.nome['nome'].title()}")
        print(f"Status da Conta: {self.nome['status'].title()}")
        print(f"Número da Conta: {self.nome['numero']}")
        print(f"Saldo da Conta: {self.nome['saldo']}")

    def mudarStatus(self):

        self.nome['status'] = 'desativado'

    def deposito(self, valor_deposito):

        self.valor_deposito = valor_deposito
        self.nome['saldo'] = self.nome['saldo'] + self.valor_deposito

    def saque(self, valor_saque):

        self.valor_saque = valor_saque

        if self.valor_saque <= self.nome['saldo']:

            self.nome['saldo'] = self.nome['saldo'] - self.valor_saque

        else:

            print("ERRO 777")

    # Para conferir.

    def mostrarDict(self):

        print(self.nome)



