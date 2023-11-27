lista_de_nomes = []

flag = True

while flag:

    print ('Digite "n" para sair.')
    nome_inserido = input("Digite um nome: ")


    if nome_inserido == "":

        print ("Não pode inserir um valor vazio.")

    elif nome_inserido.lower() == "n":

        print ("Saindo.")
        flag = False

    elif nome_inserido in lista_de_nomes:

        print ("Nome já inserido.")

    else:

        lista_de_nomes.append(nome_inserido)

    print (f"\nExistem {len(lista_de_nomes)} nomes na lista.")

    print ("\nOs nomes são: ")

    for nome in lista_de_nomes:

        print(f"\t{nome.title()}")

    print("\n")