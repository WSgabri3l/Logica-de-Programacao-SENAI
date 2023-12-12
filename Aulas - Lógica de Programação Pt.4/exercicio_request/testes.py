import requests

respostas = requests.get('https://jsonplaceholder.typicode.com/users')

if respostas.status_code == 200:

    dados = respostas.json()

postagens = requests.get('https://jsonplaceholder.typicode.com/posts?userID={usuario_id}')

if postagens.status_code == 200:

    posts = postagens.json()

print(dados)

print("\n\n\n\n\n\n")

print(posts)

print("\n\n\n\n\n\n")

print(posts[1]['title'])

id_usuario = int(input("ID do Usuário: "))

print(posts[id_usuario]['title'])
print(posts[id_usuario]['body'])

for post in posts:
        
    if post['userId'] == id_usuario:
        
        print(post['title'])
        print(post['body'])
        print("\n")

