lista_usuarios = []
lista_usuarios_nomes = []
lista_usuarios_idades = []

ativado = True

while(ativado):

    print ("1) Cadastrar usuário.")
    print ("2) Listar usuários.")
    print ("3) Sair.")

    escolha = input ("Número: ")
    escolha = int(escolha)


    if escolha == 1:
        
        #Recebe o nome.
        nome = input("Digite o nome de usuário: ")

        #Recebe a idade.
        idade = input ("Qual a idade do usuário? ")


        if nome in lista_usuarios_nomes and idade in lista_usuarios_idades:
            
            print("INVALIDO")

        else:

            #Guarda o nome e idade em uma lista para verificações e listagem de dados.
            lista_usuarios_nomes.append(nome)
            lista_usuarios_idades.append(idade)

            #Transforma o nome em um dicionário e cria uma copia para guardá-la.
            nome_copia = nome
            nome = {}

            #Adicionando o nome a lista de dados dos usuários.
            lista_usuarios.append(nome)

            #Adiciona os demais dados ao dicionário.
            nome['nome'] = nome_copia            
            nome['idade'] = idade

            localidade = input ("Qual a localidade do usuário? ")
            nome['localidade'] = localidade

            salario = input ("Qual o salario do usuario? ")
            nome['salario'] = salario


    elif escolha == 2:

        for dados in lista_usuarios:
                    
                nome = dados['nome']
                idade = dados['idade']
                localidade = dados['localidade']
                salario = dados['salario']

                print("Nome:", nome)
                print("Idade:", idade)
                print("Localidade:", localidade)
                print("Salário:", salario)
        
        print("")
            
                
    elif escolha == 3:

        print ("\nSaindo...")
        ativado = False




