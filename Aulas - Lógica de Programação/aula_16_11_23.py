numeros = []
maior = 0

while len(numeros) < 5:

    numero = input("Digite um número: ")
    numero = int(numero)
    numeros.append(numero)

for num in numeros:

    if num > maior:

        maior = num

    elif num < maior:

        maior = maior

    else:

        maior = num

print (numeros)

print (maior)