flag = True
prompt = "Deseja continuar? (Y/N)"
prompt += "\nEscolha: "

while flag:

    nome = input("Seu nome: ")

    altura = input("Altura em METROS: ")
    altura = float(altura)

    peso = input("Peso em KILOGRAMAS: ")
    peso = float(peso)

    imc = peso / altura ** 2
    imc = round(imc, 2)

    if imc < 18.50:

        print("IMC:", imc)
        classificacao = "Baixo peso."
        print(classificacao)

    elif imc >= 18.50 and imc < 24.99:

        print("IMC:", imc)
        classificacao = "Normal."
        print(classificacao)

    elif imc >= 25 and imc < 29.99:

        print("IMC:", imc)
        classificacao = "Sobrepeso."
        print(classificacao)

    else:

        print("IMC:", imc)
        classificacao = "Obesidade."
        print(classificacao)

    f = open("imc.txt", "a")
    f.write(f"{nome.title()} -->")
    f.write(f"\nIMC: {imc}")
    f.write(f"\n{classificacao}\n")
    f.write(" ")
    f.close()

    print("")

    pergunta = input(prompt)

    if pergunta.upper() == "Y":

        continue

    else:

        flag = False 