num = int(input("Número: "))
num_copia = num

calculo = 1
calculo_demonstracao = ""

for num_copia in range(num_copia, 0, -1):

    calculo_demonstracao += f"{str(num_copia)} x "

if num <= 1:

    print(f"{num}! = 1")

else:

    for n in range(1, num + 1):

        calculo = calculo * n

    print(f"{num}! = {calculo_demonstracao[0 : -3]} = {calculo}")