class Fatorial:

    def __init__(self, num):

        #self.num = int(input("Número: "))   
        self.num = num

    def calculo(self):

        self.resultado = 1

        if self.num > 1:

            for self.num in range(1, self.num + 1):

                self.resultado = self.resultado * self.num

        else:

            self.resultado = 1

        return self.resultado

    def formatar_calculo(self):

        self.num_copia = self.num
        self.calculo_demonstracao = ""

        for self.num_copia in range(self.num_copia, 0, -1):

            self.calculo_demonstracao += f"{str(self.num_copia)} x "

        self.calculo_demonstracao_ex = self.calculo_demonstracao[0 : -3]

        return self.calculo_demonstracao_ex
    
    def tabela(self):

        for self.num_copia in range(1, self.num_copia + 1):

            print(f"{self.num_copia}! = {self.calculo_demonstracao_ex} = {self.resultado}")

#numero_1 = Fatorial(1)
#print(f"{numero_1.num}! = {numero_1.formatar_calculo()} = {numero_1.calculo()}")

for num in range(1, 21):

    numero = Fatorial(num)

    print(f"{numero.num}! = {numero.formatar_calculo()} = {numero.calculo()}")
