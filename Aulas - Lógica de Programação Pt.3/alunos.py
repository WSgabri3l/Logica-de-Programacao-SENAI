class Aluno:

    def __init__(self, notas):

        self.notas = notas
        
    def calculo_media(self):

        self.media = sum(self.notas) / len(self.notas)
        self.media = round(self.media, 2)
        print(f"Média: {self.media}")

    def verificacao(self):

        if self.media >= 7:

            print("APROVADO!!!")

        else:

            print("REPROVADO!!!")