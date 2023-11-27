class Carro:

    def __init__(self, modelo):

        self.modelo = modelo
        self.velocidade = 0

    def velocidade_inicial (self):

        self.velocidade = input("Qual a velocidade? ")
        self.velocidade = int(self.velocidade)

    def acelerar (self):

        self.velocidade = self.velocidade + 1

    def frear (self):

        if self.velocidade > 1:

            self.velocidade = self.velocidade - 1 

        else:

            self.velocidade = 0

    def velocidade_atual (self):

        return self.velocidade