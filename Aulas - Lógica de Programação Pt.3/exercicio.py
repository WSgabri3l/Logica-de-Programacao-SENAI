from alunos import Aluno

nome = input("Nome do aluno: ")

idade = input("Idade do aluno: ")
idade = int(idade)

notas = []

coleta_notas = True
indice = 1

while coleta_notas:

    nota = input(f"\nNota {indice}: ")
    nota = int(nota)

    notas.append(nota)

    repetir = input("\nGostaria de adicionar outras notas? (Y/N) ")

    if repetir.upper() == "N":

        coleta_notas = False

    indice += 1

media = Aluno(notas = notas)

print(f"\nAluno: {nome.title()}")
print(f"Idade: {idade}")
media.calculo_media()

media.verificacao()