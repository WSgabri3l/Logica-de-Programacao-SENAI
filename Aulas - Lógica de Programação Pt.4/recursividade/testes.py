num = int(input("Número: "))
lista = ""

for num in range(num, 0, -1):

    lista += f"{str(num)} x "


print(lista[0 : -2]) 

    