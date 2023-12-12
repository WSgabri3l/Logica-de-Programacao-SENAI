import cadastro_alunos_funcoes 

nome = input("\nDigite o nome do aluno: ")
nome = nome.title()

sobrenome = input("\nDigite o sobrenome do aluno: ")
sobrenome = sobrenome.title()

nome_completo = f"{nome} {sobrenome}"

notas = []

#{nome.title()} {sobrenome.title()}

while True:

    nota = float(input("\nDigite um das notas: "))

    notas.append(nota)

    pergunta = input("Deseja adicionar mais alguma? (S/N) ")

    if pergunta.upper() == 'N':

        break


pergunta_2 = input("\nExiste uma nota extra? (S/N) ")

if pergunta_2.upper() == 'S':

    nota_extra = float(input("\nDigite a nota extra: "))

else:

    nota_extra = None


pergunta_3 = input("\nAluno presente? (S/N) ")

if pergunta_3.upper() == 'S':

    presenca  = "PRESENTE"

else:

    presenca = "AUSENTE"


media = cadastro_alunos_funcoes.calculo_media(notas = notas, nota_extra = nota_extra)

conceito = cadastro_alunos_funcoes.conceito(media = media)

dados_aluno = cadastro_alunos_funcoes.cadastro_aluno(nome = nome_completo, 
                                                    #sobrenome = sobrenome, 
                                                     notas = notas, 
                                                     nota_extra = nota_extra, 
                                                     presenca = presenca, 
                                                     media = media, conceito = conceito)

for categoria, informacao in dados_aluno.items():

    print(f"\n{categoria.upper()}: {informacao}")