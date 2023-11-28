from conta import Conta

ativado = True

while ativado:

    print("\n1) Criar conta.")
    print("2) Dados da conta.")
    print("3) Exibir saldo.")
    print("4) Depósito.")
    print("5) Saque.")
    print("6) Mudar status.")

    opcao = input("Opção: ")
    opcao = int(opcao)

    if opcao == 1:

        print("")

        nome_usuario = input("Digite o seu nome: ")

        nome_usuario = Conta(nome = nome_usuario)

        nome_usuario.criarConta()

        print("")

    if opcao == 2:

        print("")
        nome_usuario.dadosConta()
        print("")

    if opcao == 3:

        print("")
        nome_usuario.exibirSaldo()
        print("")

    if opcao == 4:

        valor_dep = input("Valor do Depósito: ")
        valor_dep = int(valor_dep)

        nome_usuario.deposito(valor_deposito = valor_dep)

    if opcao == 5:

        valor_saq = input("Valor do Saque: ")
        valor_saq = int(valor_saq)

        nome_usuario.saque(valor_saque = valor_saq)

    if opcao == 6:

        nome_usuario.mudarStatus()

    pergunta = input("\nAlgo mais? (S/N) ")

    if pergunta.upper() == 'N':

        ativado = False

print("\nSee you next time...")
print("esse é o nosso mundo, o que é demais nunca é o bastante!")
nome_usuario.mostrarDict()