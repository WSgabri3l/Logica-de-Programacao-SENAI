# A atividade precisa apenas no ID e do nome.
# Para as respostas, usar o ID do usuário.

#Captura de dados:

import requests

respostas = requests.get('https://jsonplaceholder.typicode.com/users')

if respostas.status_code == 200:

    dados = respostas.json()

postagens = requests.get('https://jsonplaceholder.typicode.com/posts?userID={usuario_id}')

if postagens.status_code == 200:

    posts = postagens.json()

# print(dados)
# print(posts)

# ---------------------------------------------------------------------------------------------------------------- #

# Exibir lista de Usuários:

for dado in dados:

    print(f"{dado['id']} - {dado['name']}.")

    #print(dado['id'], dado['name'])

# Menu de opções:

menu = "\n___MENU___"
menu += "\n1. Exibir post."
menu += "\n2. Listar usuários."
menu += "\n3. Sair."

loop_ativado = True

while loop_ativado:

    print(menu)

    opcao = int(input("\nEscolha: "))

    if opcao == 1:
        
        # Exibir os posts de alguém escolhido pelo usuário.

        # Receber o ID.

        id_usuario = int(input("ID do Usuário: "))

        if id_usuario > 0 and id_usuario <= 10:

            for post in posts:

                if post['userId'] == id_usuario:

                    print(f"\nTítulo: {post['title'].title()}")
                    print(f"{post['body'].capitalize()}.")

        else:

            print("\nUSUÁRIO INVÁLIDO!!!")

    if opcao == 2:

        # Exibe o nome dos usuários novamente.

        for dado in dados:

            print(f"{dado['id']} - {dado['name']}.")

    if opcao == 3:

        # Sai do loop e finaliza o programa.

        print("\nSaindo...")
        loop_ativado = False

    else:

        continue
