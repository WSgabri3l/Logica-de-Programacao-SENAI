from carros import Carro

meucarro = Carro(modelo = "Fiat Uno")

meucarro.velocidade_inicial()

meucarro.acelerar()
meucarro.acelerar()
meucarro.acelerar()

print(meucarro.velocidade_atual())

meucarro.frear()

print(meucarro.velocidade_atual())