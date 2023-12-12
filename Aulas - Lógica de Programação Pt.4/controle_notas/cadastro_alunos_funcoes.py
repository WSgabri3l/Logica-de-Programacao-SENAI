def cadastro_aluno(nome, notas, nota_extra = None, presenca = None, media = None, conceito = None):

    """Cria um dicionário com as informações de um determinado aluno."""

    aluno_dados = {

        'nome' : nome,
        #'sobrenome' : sobrenome,
        'notas' : notas,
        'nota_extra' : nota_extra,
        'presenca' : presenca,
        'media' : media,
        'conceito' : conceito

    }

    return aluno_dados

def calculo_media(notas, nota_extra = None):

    """Calcula a media das notas."""

    if nota_extra:

        media = sum(notas) / len(notas)
        media = media + nota_extra

    else:

        media = sum(notas) / len(notas)

    return media

def conceito(media):

    """Diz se o aluno foi aprovado ou não."""

    if media >= 7:

        conceito = "APROVADO"

    else:

        conceito = "REPROVADO"

    return conceito