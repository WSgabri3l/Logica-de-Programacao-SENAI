numero = input("Desejas a tabuada de qual numero? ")
numero = float(numero)

for num in range(0, 11):

    print(f"{numero} X {num} =", num * numero)