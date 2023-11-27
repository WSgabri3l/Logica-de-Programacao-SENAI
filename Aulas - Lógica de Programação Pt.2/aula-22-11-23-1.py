def numeros ():
    num_1 = input("Primeiro número: ")
    num_2 = input("Segundo número: ")

    return [num_1, num_2]

def soma ():

    nums = numeros()
    print(f"Resultado = {int(nums[0]) + int(nums[1])}")

def subtracao ():

    nums = numeros()
    print(f"Resultado = {int(nums[0]) - int(nums[1])}")

def multiplicacao ():

    nums = numeros()
    print(f"Resultado = {int(nums[0]) * int(nums[1])}")

def divisao ():

    nums = numeros()
    print(f"Resultado = {int(nums[0]) / int(nums[1])}")

ativado = True

while(ativado):

    print("Operações disponíveis: ")
    print("1) Soma.")
    print("2) Subtração.")
    print("3) Multiplicação.")
    print("4) Divisão.")
    print("5) Sair.")

    opcao = input("Opção: ")
    opcao = int(opcao)

    if opcao == 1:

        soma()

    if opcao == 2:
        
        subtracao()

    if opcao == 3:

        multiplicacao()

    if opcao == 4:

        divisao()

    if opcao == 5:

        ativado = False